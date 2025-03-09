import cv2
import numpy as np

#read an image
img=cv2.imread("images/image1.png")

cv2.imshow("window", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

## covert RGB image into grayscale image
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window2",img_gray)
cv2.waitKey(1000)

##BGR to RGB
## in opencv image is in BGR format
img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("window2",img_RGB)
cv2.waitKey(1000)
cv2.destroyAllWindows()

## bgr to black and white
## firt we need to convert it into grayscale and then into black and white

image_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,image_BW=cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("BLACK AND WHITE",image_BW)
cv2.waitKey(1000)
cv2.destroyAllWindows()