import cv2
import numpy
import numpy as np

PREVIEW = 0#preview mode
BLUR = 1#Blurring filter
FEATURES = 2 #corner feature detector
CANNY = 3 # canny edge detector
win_name=cv2.namedWindow("window")
feature_params=dict(
    maxCorners=500,
    qualityLevel=0.2,
    minDistance=15,
    blockSize=9)

image_filter = PREVIEW
alive = True
cap=cv2.VideoCapture(0)

while alive:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.flip(frame,1)
    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result=cv2.Canny(frame,100,250)
    elif image_filter == BLUR:
        result = cv2.blur(frame,(13,13))
    elif image_filter == FEATURES:
        result = frame
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        corners=cv2.goodFeaturesToTrack(frame_gray,**feature_params)
        if corners is not None:
            for x,y in numpy.float32(corners).reshape(-1,2):
                cv2.circle(result,(int(x),int(y)),10,(0,255,0),1)
    cv2.imshow(win_name,result)
    key=cv2.waitKey(1)
    if key == ord('q') or key == ord('Q') or key == 27:
        alive =False
    elif key == ord("C") or key == ord('c'):
        image_filter = CANNY
    elif key == ord('B') or key == ord("b"):
        image_filter = BLUR
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW
cap.release()
cv2.destroyAllWindows()


