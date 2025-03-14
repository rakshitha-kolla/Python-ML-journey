import cv2
import numpy as np
#read image
img=cv2.imread("images/objd2.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
edges=cv2.Canny(blurred,100,200)
contours,hierarchy=cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt)>100:
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)
cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()