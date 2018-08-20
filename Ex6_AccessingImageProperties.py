# Program for image properties and color planes


import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('lena_color_512.tif',1)

plt.imshow(img, cmap='gray')
plt.show()


#cv2.imshow('Lena',img)

size = img.shape  # size of image
print size

t = img.dtype # image datatype
print t

#roi = img[280:340, 330: 390]  # for roi
#img[173:233, 100:160] = roi
#cv2.imshow('Lena1',img)
#cv2.imshow('Region of interest',roi) 


# spliting and merging color channels

#b,g,r = cv2.split(img) # splitting
#cv2.imshow('blue',b)
#img = cv2.merge((b,g,r)) 


# Another approach

#b = img[:,:,0]
#cv2.imshow('blue1',b)
#img[:,:,2] = 0  # This can be used to separate color planes
#img[:,:,1] = 0
#cv2.imshow('blue_image',img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
