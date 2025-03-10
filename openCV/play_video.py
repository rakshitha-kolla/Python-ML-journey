import cv2
import time
cap=cv2.VideoCapture("webcam_output.avi")
while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        break
    time.sleep(1/20)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
cap.release()
cv2.destroyAllWindows()