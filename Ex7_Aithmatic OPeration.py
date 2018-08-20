import cv2
import numpy as np

from matplotlib import pyplot as plt

img1 = cv2.imread('image1.bmp');
img2 = cv2.imread('image2.bmp');


addition = cv2.add(img1,img2)

plt.subplot(131), plt.imshow(img1), plt.title('Image1')
plt.subplot(132), plt.imshow(img2), plt.title('Image2')
plt.subplot(133), plt.imshow(addition), plt.title('Addition')
plt.show()


#cv2.imshow('addition of image',addition)

cv2.waitKey(0)
cv2.destroyAllWindows() 

