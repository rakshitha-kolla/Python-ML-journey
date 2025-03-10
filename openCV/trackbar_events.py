import cv2
import numpy as np
def change_brightness(val):
    brightness = val-100
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(hsv)
    v=np.clip(v.astype(np.int16) + brightness,0,255).astype(np.uint8)
    hsv_adjusted=cv2.merge((h,s,v))
    img_adjusted = cv2.cvtColor(hsv_adjusted,cv2.COLOR_HSV2BGR)
    cv2.imshow("Tracker Window",img_adjusted)
original=cv2.imread("images/image1.png",cv2.IMREAD_COLOR)
shape=original.shape
img=cv2.resize(original,(shape[1]//2,shape[0]//2))
cv2.namedWindow("Tracker Window")
cv2.createTrackbar("Brightess","Tracker Window",100,200,change_brightness)
cv2.imshow("Tracker Window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()