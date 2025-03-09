import cv2
import numpy as np

# create image

img=np.zeros((512,512,3))

# draw rectangle( pt1=(x1,y1) pt2=(x2,y2),color,thickness)
# rectangle x2-x1 != y2-y1 i.e height != weight
# here 200-50 = 150 and 150-50=100 not equal so rectangle shape
cv2.rectangle(img,pt1=(50,50),pt2=(200,150),color=(255,0,0),thickness=3)

cv2.imshow("window",img)
cv2.waitKey(1000)

# draw square
#x2-x1 = y2-y2
# 300-100 = 200
# 300-100 =200
# so square if thickness=-1 then fill inner part of shape
img=np.zeros((512,512,3))
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)
cv2.imshow("window",img)
cv2.waitKey(1000)

img=np.zeros((512,512,3))
# draw circle (center_x,center_y,radius)
img=np.zeros((512,512,3))
cv2.circle(img,(150,300),50,(0,0,255),3)
cv2.imshow("window",img)
cv2.waitKey(1000)

# elipse (center,axes,angle,startangle,endangle)
# center -> (x,y)
# axes -> (major_axis_length,minor_axis_length)(half-lenghths of ellipse axes)
# -> major axis makes ellipse wider and minor axis makes ellipse taler
# angle -> rotation angle of ellipse in degrees
# startangle -> starting angle from where the arc begins
# endangle -> ending angle where the arc stops

cv2.ellipse(img,(350,300),(80,40),40,0,360,(0,255,255),3)
cv2.imshow("window",img)
cv2.waitKey(1000)

cv2.ellipse(img,(250,250),(100,50),0,0,180,(0,255,255),-1)
cv2.imshow("window",img)
cv2.waitKey(1000)


# draw a line(start_point,end_point)
cv2.line(img,(100,400),(400,400),(255,0,0),3)
cv2.imshow("window",img)
cv2.waitKey(1000)


# add text
# cv2.putText(image,text,org,font,fontscale,color,thickness,lineType)
# org -> bottom left corner of text
# font -> fontstyle
# fontScale -> size of text
# lineType -> type of line (cv2.LINE_AA for anti-aliased text)
cv2.putText(img,org=(100,100),fontScale=4,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA,fontFace=cv2.FONT_ITALIC,text="hello")
cv2.imshow("window",img)
cv2.waitKey(1000)