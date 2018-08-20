#Program for averaging and Gaussian blur images


import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy


img = cv2.imread('opencv_logo.png')

#blur = cv2.blur(img,(5,5)) # for Averaging
blur = cv2.GaussianBlur(img,(5,5),0) # for Gaussian Blur

print blur

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
