import cv2
import numpy as np
img=cv2.imread("images/noisy2.png")
cv2.imshow("original image",img)
# average blurring
img_blur=cv2.blur(img,(7,7))
cv2.imshow("blur image",img_blur)
#gaussian blur
img_gaussian_blur=cv2.GaussianBlur(img,(5,5),3)
cv2.imshow("Gausssian Blur",img_gaussian_blur)
#median blur
img_median_blur=cv2.medianBlur(img,7)
cv2.imshow("median blur",img_median_blur)
cv2.waitKey(0)