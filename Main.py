from PIL import Image, ImageEnhance, ImageOps
import numpy as np

img = Image.open("bird.jpg")
img = ImageEnhance.Contrast(img).enhance(30.0)
img = ImageEnhance.Sharpness(img).enhance(2.0)

# Make image greyscale to ensure only pixel intensities are represented
img = ImageOps.grayscale(img)

sobel_img = Image.new("L", ([img.size[0]-1, img.size[1]-1]), 255)

# get all convolution kernel anchor positions within the image
anchor_positions = []

for w in range(1, img.size[0]-1):
    for h in range(1, img.size[1]-1):
        anchor_positions.append((w, h))

def xDirKernel(top_left: int, top_center:int, top_right: int, 
               left: int, center: int, right: int, 
               bottom_left: int, bottom_center: int, bottom_right: int):
    
    outputs = []
    outputs.extend((top_left * -1, top_center * 0, top_right, 
                    left * -2, center * 0, right * 2,
                    bottom_left * -1, bottom_center * 0, bottom_right))
    
    return outputs

def yDirKernel(top_left: int, top_center:int, top_right: int, 
               left: int, center: int, right: int, 
               bottom_left: int, bottom_center: int, bottom_right: int):
    
    outputs = []
    outputs.extend((top_left * -1, top_center * -2, top_right * -1, 
                    left * 0, center * 0, right * 0,
                    bottom_left, bottom_center * 2, bottom_right))
    
    return outputs


def SumKernel(kernelOutputs: list):
    return np.sum(kernelOutputs)

def GetGradientMag(gX: int, gY: int):
    gXsqr = gX * gX
    gYsqr = gY * gY
    sqrSum = gXsqr + gYsqr
    gMag = np.sqrt(sqrSum)
    
    return gMag

for i in range(len(anchor_positions)):
    x = anchor_positions[i][0]
    y = anchor_positions[i][1]

    top_left = img.getpixel((x-1, y-1))
    top_center = img.getpixel((x, y-1))
    top_right = img.getpixel((x+1, y-1))
    left = img.getpixel((x-1, y))
    center = img.getpixel((x, y))
    right = img.getpixel((x+1, y))
    bottom_left = img.getpixel((x-1, y+1))
    bottom_center = img.getpixel((x, y+1))
    bottom_right = img.getpixel((x+1, y+1))
    
    xKernelOutputs = xDirKernel(top_left, top_center, top_right,
                                left, center, right,
                                bottom_left, bottom_center, bottom_right)

    yKernelOutputs = yDirKernel(top_left, top_center, top_right,
                                left, center, right,
                                bottom_left, bottom_center, bottom_right)

    gradientX = SumKernel(xKernelOutputs)
    gradientY = SumKernel(yKernelOutputs)

    gradientMag = GetGradientMag(gradientX, gradientY)

    if gradientMag > 300:
        sobel_img.putpixel(anchor_positions[i], (0))

img.show()
sobel_img.show()


