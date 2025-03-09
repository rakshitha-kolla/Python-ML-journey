import cv2
import numpy as np


#read an image
img=cv2.imread("images/image1.png")
print(type(img))
print(img.shape)
print("printing image")
print(img)
print()

cv2.imshow("window", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()