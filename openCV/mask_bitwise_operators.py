#mask an image
#mask is binary(black and white) image used to control which part of an image should be visible or modified.
#white pixels(255)-> allows the corresponding image pixels to be visible
#black pixels(0)-> block the corresponding image pixels(turn them black in output)
import cv2
import numpy as np

img=cv2.imread("images/image1.png")
mask = np.zeros(img.shape[:2],dtype=np.uint8)
cv2.circle(mask,(150,150),100,255,-1)
result=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("bitwise_and",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
img1=cv2.imread("images/mask1.jpeg")
img2=cv2.imread("images/mask2.jpg")
img2= cv2.resize(img2,(img1.shape[1],img1.shape[0]))
img1_bw=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,img1_bw=cv2.threshold(img1_bw,127,255,cv2.THRESH_BINARY)
img1_bw_inv=cv2.bitwise_not(img1_bw)
cv2.imshow("img1_bw",img1_bw)
cv2.imshow("img1_bw_inv",img1_bw_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
img_background=cv2.bitwise_and(img2,img2,mask=img1_bw)
img_foreground=cv2.bitwise_and(img1,img1,mask=img1_bw_inv)
cv2.imshow("img_background",img_background)
cv2.imshow("img_foreground",img_foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()

result=cv2.add(img_foreground,img_background)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()