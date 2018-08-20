# Structuring element

"""
We manually created a structuring elements in the previous examples with help
of Numpy. It is rectangular shape. But in some cases, you may need elliptical/
circular shaped kernels. So for this purpose, OpenCV has a function,
cv2.getStructuringElement(). You just pass the shape and size of the kernel,
you get the desired kernel.

"""

import cv2
import numpy as np


# Rectangular Kernel
rect = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# Elliptical Kernel
ellipt = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# Cross-shaped Kernel
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

print rect
print ellipt
print cross
