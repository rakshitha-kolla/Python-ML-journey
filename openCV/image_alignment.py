'''import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
ref_img=cv2.imread("images/reference.jpg",cv2.IMREAD_GRAYSCALE)
input_img=cv2.imread("images/input_img.jpg",cv2.IMREAD_GRAYSCALE)
ref_img=cv2.resize(ref_img, (ref_img.shape[1]//4, ref_img.shape[0]//4))
input_img=cv2.resize(input_img,(input_img.shape[1]//4,input_img.shape[0]//4))
cv2.imshow("reference_image",ref_img)
cv2.imshow("input_image",input_img)
cv2.waitKey(0)

#initialize ORB detector
orb=cv2.ORB_create()
#Detect Keypoints and compute Descriptors (imh,mask)
kp1,des1=orb.detectAndCompute(ref_img,None)
kp2,des2=orb.detectAndCompute(input_img,None)


# Check if keypoints are found
if len(kp1) == 0 or len(kp2) == 0:
    print("No keypoints found in one of the images.")
    exit()


#Match Features using BFMatcher (Brute Force Matcher) with Hamming Distance

df=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches= df.match(des1,des2)

#sort matches by distance (best matches first)
matches = sorted(matches,key=lambda x: x.distance)

#select top 50 matches
good_matches = matches[:50]

# Extract matched keypoints
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

#compute homography matrix
H,_=cv2.findHomography(src_pts,dst_pts,cv2.RANSAC)

#wrap the input image to align it with the reference image
h,w = ref_img.shape
aligned_img=cv2.warpPerspective(input_img,H,(w,h))
cv2.imshow("refence_image",ref_img)
cv2.imshow("input_image",input_img)
cv2.imshow("aligned_image",aligned_img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
import cv2
import numpy as np

# Load images
ref_img = cv2.imread("images/reference.jpg", cv2.IMREAD_GRAYSCALE)
input_img = cv2.imread("images/input_img.jpg", cv2.IMREAD_GRAYSCALE)

# Resize images to 25% for faster processing
ref_img = cv2.resize(ref_img, (ref_img.shape[1] // 4, ref_img.shape[0] // 4))
input_img = cv2.resize(input_img, (input_img.shape[1] // 4, input_img.shape[0] // 4))

# Initialize SIFT detector (better for rotation)
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(ref_img, None)
kp2, des2 = sift.detectAndCompute(input_img, None)

if len(kp1) == 0 or len(kp2) == 0:
    print("No keypoints found in one of the images.")
    exit()

# Use FLANN-based matcher (faster for SIFT)
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Apply Lowe's ratio test to filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

if len(good_matches) < 10:
    print("Not enough good matches found.")
    exit()

# Extract matched keypoints
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Compute homography matrix
H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC)

# Apply perspective transformation
h, w = ref_img.shape
aligned_img = cv2.warpPerspective(input_img, H, (w, h))

# Show results
cv2.imshow("Reference Image", ref_img)
cv2.imshow("Input Image", input_img)
cv2.imshow("Aligned Image", aligned_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
