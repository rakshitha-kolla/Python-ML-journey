import cv2
import numpy as np

# function handles events
def draw(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+40,y+40),(0,255,0),-1)
# read
img=np.zeros((512,512,3))

cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)

# waitKey() returns ascii of pressed key on keyboard 0XFF is used to ensure only 8  bits represent aactual ascii value of key pressed

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()