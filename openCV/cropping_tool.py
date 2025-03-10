import numpy as np
import cv2

def crop(event,x,y,flags,param):
    global start_x, start_y, end_x, end_y, drawing, cropped_img, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        start_x=x
        start_y=y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy=img.copy()
            cv2.rectangle(img_copy,(start_x,start_y),(x,y),(0,0,255),2)
            cv2.imshow("cropping",img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        end_x=x
        end_y=y
        start_x,end_x=min(start_x,end_x),max(start_x,end_x)
        start_y,end_y=min(start_y,end_y),max(start_y,end_y)

        cropped=img[start_y:end_y,start_x:end_x]
        if cropped.size>0:
            cv2.imshow("window",cropped)
# read image
original=cv2.imread("images/image2.png")
img=cv2.resize(original,(original.shape[1]//2,original.shape[0]//2))
cv2.namedWindow("cropping")
cv2.setMouseCallback("cropping",crop)
while True:
    cv2.imshow("cropping",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()