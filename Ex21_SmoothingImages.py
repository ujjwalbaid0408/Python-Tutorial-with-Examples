#Program for smoothing images


import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy

img = cv2.imread('opencv_logo.png',1)
row,col,plane = img.shape
print row, col, plane

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
row,col,plane = dst.shape
print row, col, plane


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

 
cv2.waitKey(0)
cv2.destroyAllWindows()
