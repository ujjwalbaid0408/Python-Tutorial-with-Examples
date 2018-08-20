# Making Borders for Images (Padding)

import cv2
import numpy as np
#import numpy

from matplotlib import pyplot as plt

BLUE = [ 255,0,0]

img1 = cv2.imread('opencv_logo.png')
#img1 = numpy.matrix('1 2 3; 4 5 6; 7 8 9')

# Similar to pixel replication
replicate = cv2.copyMakeBorder(img1, 1,1,1,1, cv2.BORDER_REPLICATE)

# By relecting the pixels
reflect = cv2.copyMakeBorder(img1, 1,1,1,1, cv2.BORDER_REFLECT)

# By Border Reflect_101
reflect101 = cv2.copyMakeBorder(img1,1,1,1,1,cv2.BORDER_REFLECT_101)

# by wrap
wrap = cv2.copyMakeBorder(img1,1,1,1,1,cv2.BORDER_WRAP)

# By constant
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
# See the result below. (Image is displayed with matplotlib 
# so RED and BLUE planes will be interchanged):

# constant= cv2.copyMakeBorder(img1,1,1,1,1,cv2.BORDER_CONSTANT,value=100)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
