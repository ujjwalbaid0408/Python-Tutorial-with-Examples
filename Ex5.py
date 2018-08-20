# This program is to read and modify the pixels in an image

import cv2
import numpy as np

img = cv2.imread('lena_color_512.tif')

# Access a pixel value by its row and column coordinates
px = img[100,100]
print px

# accessing only blue pixel
blue = img[100,100,0]    # 0= Blue 1=Green 2=Red
print blue

# Modify the pixel values
img[100,100] = [255,255,255]
print img[100,100]

# Better pixel accessing and editing method
# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)
