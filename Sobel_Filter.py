from PIL import Image, ImageEnhance, ImageOps
import numpy as np

def getImg(file_path: str):
    img = Image.open(file_path)
    return img

def getAnchorPositions(width: int, height: int):
    # get all convolution kernel anchor positions within the image
    anchor_positions = []

    for w in range(1, width-1):
        for h in range(1, height-1):
            anchor_positions.append((w, h))
    
    return anchor_positions

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
    return int(np.sum(kernelOutputs))

def GetGradientMag(gX: int, gY: int):
    gXsqr = gX * gX
    gYsqr = gY * gY
    sqrSum = gXsqr + gYsqr
    gMag = np.sqrt(sqrSum)
    
    return gMag




