# Program for affine transform

"""
In affine transformation, all parallel lines in the original image will still
be parallel in the output image. To find the transformation matrix, we need
three points from input image and their corresponding locations in output image.
Then cv2.getAffineTransform will create a 2x3 matrix which is to be passed to
cv2.warpAffine.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cameraman.tif')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
print M
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
