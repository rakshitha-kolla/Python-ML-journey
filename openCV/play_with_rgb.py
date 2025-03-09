import cv2
import numpy as np

##read image
original=cv2.imread("images/image2.png")
shape=original.shape
## above image too large it doesn't fit in window so resize it
## resizing image
img=cv2.resize(original,(shape[1]//2,shape[0]//2))

# display image
cv2.imshow("display image",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

img_blue=img.copy()
img_green=img.copy()
img_red=img.copy()
img_blue[:,:,0]=0
img_green[:,:,1]=0
img_red[:,:,2]=0
# blue channel is 0
cv2.imshow("no blue",img_blue)
cv2.waitKey(1000)
cv2.destroyAllWindows()

## green channel is 0
cv2.imshow("no green",img_green)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# red channel is 0
cv2.imshow("no red",img_red)
cv2.waitKey(1000)
cv2.destroyAllWindows()



## now display only specific channey
blue=img.copy()
green=img.copy()
red=img.copy()
blue[:,:,1]=0
blue[:,:,2]=0
green[:,:,0]=0
green[:,:,2]=0
red[:,:,0]=0
red[:,:,1]=0
cv2.imshow("blue channel",blue)
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.imshow("green channel",green)
cv2.waitKey(1000)
cv2.destroyAllWindows()

cv2.imshow("red channel",red)
cv2.waitKey(1000)
cv2.destroyAllWindows()

## below are single chnnel images
# i.e 2d arrays specifies intensity of single channel either blue or green or red
blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
new_image=np.hstack((blue,green,red))
cv2.imshow("stacked images",new_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()


## single channel to multiple channel
## cv2.merge is a function that combines multiple single-channel images into a multi-channel image.
# In this case, it combines three single-channel images into a 3-channel image (BGR format).
blue_stack=cv2.merge([blue,np.zeros_like(blue),np.zeros_like(blue)])
green_stack=cv2.merge([np.zeros_like(green),green,np.zeros_like(green)])
red_stack=cv2.merge([np.zeros_like(red),np.zeros_like(red),red])

##
new_img=np.hstack((blue_stack,green_stack,red_stack))
cv2.imshow("3channel stakced",new_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
