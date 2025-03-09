import cv2
import numpy as np

#read image
original=cv2.imread("images/image2.png")
shape=original.shape
img=cv2.resize(original,(shape[1]//2,shape[0]//2))
'''
->in openCV you can use cv2.flip() to flip images
->it has three codes called flipcodes: 0,1,-1
-> 0 is flip vertically(upside down)
-> 1 is flip horizontally(left to right)
-> -1 is flip both vertically and horizontally(180-degree rotation)
'''
img_vflip=cv2.flip(img,0)
img_hflip=cv2.flip(img,1)
img_bflip = cv2.flip(img,-1)
l=[img,img_vflip,img_hflip,img_bflip]

for img in l:
    cv2.imshow("window",img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
s=np.hstack((img_vflip,img_hflip,img_bflip))
cv2.imshow("window",s)
cv2.waitKey(0)
cv2.destroyAllWindows()