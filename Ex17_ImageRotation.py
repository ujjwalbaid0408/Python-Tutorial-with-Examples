# Program for rotatin of an image
# rotates the image by degree with respect to center without any scaling

import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),27,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Rotated Image',dst)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
