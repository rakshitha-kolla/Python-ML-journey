'''
BITWISE OPERATORS
cv2.bitwise_and(),cv2.bitwise_or(),cv2.bitwise_xor(),cv2.bitwise_not()
dst=cv2.bitwise_and(sec1,src2,dst,mask)
src1=imag1
src2=image2
mask=which part
'''
import cv2
import numpy as np
#bitwise_and

img1=np.zeros((300,300),dtype=np.uint8)
img2=np.zeros((300,300),dtype=np.uint8)
cv2.rectangle(img1,(150,0),(300,300),(255,255,255),-1)
cv2.circle(img2,(150,150),100,(255,255,255),-1)
cv2.imshow("rectangle",img1)
cv2.imshow("circle",img2)
result=cv2.bitwise_and(img1,img2)
cv2.imshow("bitwise_and",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bitwise_or
result=cv2.bitwise_or(img1,img2)
cv2.imshow("rectangle",img1)
cv2.imshow("circle",img2)
cv2.imshow("bitwise_or",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bitwise_xor
result=cv2.bitwise_xor(img1,img2)
cv2.imshow("rectangle",img1)
cv2.imshow("circle",img2)
cv2.imshow("bitwise_xor",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bitwise_not
result=cv2.bitwise_not(img2)
cv2.imshow("circle",img2)
cv2.imshow("bitwise_not",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

