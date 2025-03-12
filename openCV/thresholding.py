import cv2
import numpy as np
img=cv2.imread("images/thresh1.jpg")
print(img.shape)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_scale",img_gray)
# simple thresholding
_,thresh_gray=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("simple_threshod",thresh_gray)

# adaptive thresholding
thresh_adaptive=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,10)
cv2.imshow("adaptive_threshold",thresh_adaptive)
cv2.waitKey(0)
#simple thresholding