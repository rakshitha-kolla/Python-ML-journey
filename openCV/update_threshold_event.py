import cv2
import numpy as np

def update_threshold(val):
    _, thresholded = cv2.threshold(img_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow("tracker window", thresholded)

# Load the image in grayscale mode
img_gray = cv2.imread("images/image2.png", 0)
img_gray=cv2.resize(img_gray,(img_gray.shape[1]//2,img_gray.shape[0]//2))
# Check if the image was loaded successfully
if img_gray is None:
    print("Error: Could not load image. Please check the file path.")
    exit()

# Create a window
cv2.namedWindow("tracker window")

# Create a trackbar and link it to the update_threshold function
cv2.createTrackbar("threshold", "tracker window", 127, 255, update_threshold)

# Show the initial image
cv2.imshow("tracker window", img_gray)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()