# Morphological Transformations

"""

Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above.
Here we use the function, cv2.morphologyEx()

Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground
objects, or small black points on the object.

Morphological Gradient: 
It is the difference between dilation and erosion of an image.
The result will look like the outline of the object.

Top Hat
It is the difference between input image and Opening of the image.
Below example is done for a 9x9 kernel.

Black Hat
It is the difference between the closing of the input image and input image.
"""



import cv2
import numpy as np

#img = cv2.imread('morph1.bmp',0)
img = cv2.imread('j.jpg',0)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original', img)
cv2.imshow('Eroded',erosion)
cv2.imshow('dilated',dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing', closing)
cv2.imshow('Morphological Gradient',gradient)
cv2.imshow('Top Hat', tophat)
cv2.imshow('Black Hat',blackhat);
cv2.waitKey(0)
cv2.destroyAllWindows()
