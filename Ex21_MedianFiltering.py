#Program for Median filtering


import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy


img = cv2.imread('opencv_noise.png')
blur = cv2.medianBlur(img,5)


print blur

plt.subplot(121),plt.imshow(img),plt.title('Original with salt and pepper noise')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Median Filtered')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
