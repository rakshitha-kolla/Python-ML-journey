import cv2
import numpy as np
# read
def draw(event,x,y,flag,params):
    global drawing,start_x,start_y,img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        start_x,start_y=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_temp=img.copy()
            cv2.rectangle(img_temp,(start_x,start_y),(x,y),(0,255,0),-1)
            cv2.imshow("window",img_temp)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(start_x,start_y),(x,y),(0,255,0),-1)

img=np.zeros((512,512,3))
cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()