import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("images/image1.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

## add brightness to image
matrix=np.ones(img.shape,dtype="uint8") * 50
img_brighter=cv2.add(img,matrix)
img_darker=cv2.subtract(img,matrix)

cv2.imshow("darker",img_darker)
cv2.imshow("original",img)
cv2.imshow("brighter",img_brighter)
cv2.waitKey(0)
cv2.destroyAllWindows()