import cv2
cap=cv2.VideoCapture("webcam_output.avi")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray video",gray)
    if cv2.waitKey(30) & 0xFF == ord("x"):
        break
cap.release()
cv2.destroyAllWindows()