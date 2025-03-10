import cv2
import numpy as np

cap=cv2.VideoCapture(0)

#define video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#codec for AVI format

out=cv2.VideoWriter("webcam_output.avi",fourcc,20,(640,480))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(2) & 0xFF == ord("x"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()