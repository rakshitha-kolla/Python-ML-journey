import cv2
import numpy as np
from PIL import Image
from utils import get_limits
cap=cv2.VideoCapture(0)
yellow=[0,255,255]
while True:
    ret,frame = cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_limit,upper_limit=get_limits(yellow)
    mask=cv2.inRange(hsvImage,lower_limit,upper_limit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("z"):
        break
cv2.destroyAllWindows()
