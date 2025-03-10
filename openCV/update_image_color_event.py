import cv2
import numpy as np

def update_color(x):
    r = cv2.getTrackbarPos("R","color window")
    g = cv2.getTrackbarPos("G", "color window")
    b = cv2.getTrackbarPos("B", "color window")
    img[:]=[b,g,r]
    cv2.imshow("color window",img)
img=np.zeros((300,512,3)).astype(np.uint8)
cv2.namedWindow("color window")
cv2.createTrackbar("R","color window",0,255,update_color)
cv2.createTrackbar("G","color window",0,255,update_color)
cv2.createTrackbar("B","color window",0,255,update_color)
cv2.imshow("color window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
