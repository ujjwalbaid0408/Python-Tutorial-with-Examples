# Translation of image 



import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]]) # 100 is tx and 50 is ty wrt transformation matrix
dst = cv2.warpAffine(img,M,(cols,rows))

#cv2.imshow('img',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()