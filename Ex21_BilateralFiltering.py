#Program for Bilateral filtering


import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy


img = cv2.imread('texture.jpg')
blur = cv2.bilateralFilter(img,9,75,75)


print blur

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()
