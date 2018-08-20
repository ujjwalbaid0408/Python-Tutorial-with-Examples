import cv2
import numpy as np

from matplotlib import pyplot as plt

img1 = cv2.imread('Ujjwal_resize.jpg',1);
img2 = cv2.imread('lena.jpg');


img_blend = cv2.addWeighted(img1,0.5,img2,0.5,0)

plt.subplot(131), plt.imshow(img1), plt.title('Image1'), plt.axis('off')
plt.subplot(132), plt.imshow(img2), plt.title('Image2'), plt.axis('off')
plt.subplot(133), plt.imshow(img_blend), plt.title('Image BLending'), plt.axis('off')
plt.show()


#cv2.imshow('addition of image',addition)

cv2.waitKey(0)
cv2.destroyAllWindows() 

