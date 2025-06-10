# Libraries
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageOps, ImageTk
import os

# Script(s)
import Sobel_Filter as sf



def import_file():
    global preview
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.jpg *.png *.pdf")])
    #preview = ImageTk.PhotoImage(Image.open(file_path))

    return file_path

def generateSobelImg():
    global preview
    global sobelImg
    
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

    sobelImg = sobel_img

    im = ImageOps.fit(sobel_img, size)
    preview_sobelimg = ImageTk.PhotoImage(im)
    image_label.configure(image=[preview_sobelimg])
    image_label.image=preview_sobelimg

def ExportImg():
    try:
        dirname = os.path.dirname(__file__)
        filename = str(dirname + "/output/" + "sobel_image.png")
        sobelImg.save(filename)
        print("succcessfully exported!")
    except:
        tk.messagebox.showerror(title="Error", message="No image uploaded")
    

global sobelImg
global preview

root = tk.Tk()
root.geometry("600x440+400+250")  # Width 600, Height 400, at x=400, y=250
root.title("Sobel Filter")

root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 500
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


size = (300, 300)
im =  ImageOps.fit(Image.open("preview.png"), size)
preview = ImageTk.PhotoImage(im)
image_label = tk.Label(root, image=[preview])

upload_button = tk.Button(root, text="Upload File", command=generateSobelImg)
export_button = tk.Button(root, text="Export Sobel Image", command=ExportImg)

image_label.pack(pady=20)
upload_button.pack(padx=5, pady=5)
export_button.pack(padx=5, pady=0)

root.mainloop()


