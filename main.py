import tkinter as tk
from tkinter import * 
#from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageOps

import Sobel_Filter as sf


def import_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    return file_path

def generateSobelImg():

    img = Image.open(import_file())

    img = ImageEnhance.Contrast(img).enhance(3.0)
    img = ImageEnhance.Sharpness(img).enhance(2.0)
    # Make image greyscale to ensure only pixel intensities are represented
    img = ImageOps.grayscale(img)
    sobel_img = Image.new("L", ([img.size[0]-1, img.size[1]-1]), 255)

    anchor_positions = sf.getAnchorPositions(img.size[0], img.size[1])

    # cycle through all anchor positions
    for i in range(len(anchor_positions)):
        x = anchor_positions[i][0]
        y = anchor_positions[i][1]

        # get the pixel intensity for each pixel in the 3x3 grid, with the anchor in the center
        top_left = img.getpixel((x-1, y-1))
        top_center = img.getpixel((x, y-1))
        top_right = img.getpixel((x+1, y-1))
        left = img.getpixel((x-1, y))
        center = img.getpixel((x, y))
        right = img.getpixel((x+1, y))
        bottom_left = img.getpixel((x-1, y+1))
        bottom_center = img.getpixel((x, y+1))
        bottom_right = img.getpixel((x+1, y+1))
        
        # convolve the values with the x and y kernel matrices
        xKernelOutputs = sf.xDirKernel(top_left, top_center, top_right,
                                    left, center, right,
                                    bottom_left, bottom_center, bottom_right)

        yKernelOutputs = sf.yDirKernel(top_left, top_center, top_right,
                                    left, center, right,
                                    bottom_left, bottom_center, bottom_right)

        # sum the convolved values
        gradientX = sf.SumKernel(xKernelOutputs)
        gradientY = sf.SumKernel(yKernelOutputs)

        # calculate the magnitude of the gradient
        gradientMag = sf.GetGradientMag(gradientX, gradientY)

        # if magnitude is above threshold, means there is a sharp change in pixel intensity... 
        # means likely to be an outline therefore place a pixel at the anchor position
        if gradientMag > 300:
            sobel_img.putpixel(anchor_positions[i], (0))
        
    #img.show()
    sobel_img.show()


# Create the main Tkinter window
root = tk.Tk()
root.geometry("600x400+400+250")  # Width 600, Height 400, at x=100, y=50
root.title("Import File Example")

# Create an "Import File" button

import_button1 = tk.Button(root, text="Generate Sobel Image", command=generateSobelImg)
import_button1.pack()

# Run the Tkinter event loop
root.mainloop()


