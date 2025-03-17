import cv2
import numpy as np

img=cv2.imread("images/image1.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
matrix1=np.ones(img.shape) * .8
matrix2=np.ones(img.shape) * 2.0
img_darker=np.uint8(cv2.multiply(np.float64(img),matrix1))
img_brighter=np.uint8(np.clip(cv2.multiply(np.float64(img),matrix2),0,255))

#show images
cv2.imshow("darker",img_darker)
cv2.imshow("original",img)
cv2.imshow("brighter",img_brighter)
cv2.waitKey(0)
cv2.destroyAllWindows()