import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import glob


#read images
image_files=glob.glob("/home/apiiit123/PycharmProjects/workspace/panaroma/*.jpg")
image_files.sort()

images=[]
for filename in image_files:
    img=cv2.imread(filename)
    if img is not None:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        images.append(img)
num_images=len(images)


#Display images
plt.ion()
plt.figure(figsize=[30,10])
num_cols=1
num_rows= math.ceil(num_images / num_cols)
for i in range(num_images):
    plt.subplot(num_rows,num_cols,i+1)
    plt.axis("off")
    plt.imshow(images[i])
plt.show()

#stitch images

stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images)
if status == 0:
    plt.figure(figsize=[30, 10])
    plt.imshow(result)
    plt.axis("off")
    plt.title("Panorama")
    plt.show()

    # Save the result
    result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
    cv2.imwrite("ouput_panaroma.jpg", result_bgr)
    print(f"Stitched image saved")
else:
    print("Image stitching failed. Status code:", status)
