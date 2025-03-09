import cv2
import numpy as np

#read image
img=cv2.imread("images/image2.png")
img_crop=img[:500,0:500]
cv2.imshow("cropped image",img_crop)
cv2.waitKey(1000)

cv2.imwrite("images/cropped_image.png",img_crop)