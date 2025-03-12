import cv2
import numpy as np
ntr=cv2.imread("images/ntr.jpg",cv2.IMREAD_GRAYSCALE)
ntr=cv2.resize(ntr,(ntr.shape[1]//2,ntr.shape[0]//2))
cv2.imshow("gray",ntr)
NTR=cv2.Canny(ntr,100,200)
cv2.imshow("edge_detection",NTR)
NTR_d=cv2.dilate(NTR,np.ones((3,3),dtype=np.int8))
cv2.imshow("dilate",NTR_d)
NTR_e=cv2.erode(NTR_d,np.ones((3,3),dtype=np.int8))
cv2.imshow("erode",NTR_e)
'''
img2=cv2.imread("images/image2.png",cv2.IMREAD_GRAYSCALE)
img2=cv2.resize(img2,(img2.shape[1]//2,img2.shape[0]//2))
cv2.imshow("gray2",img2)
canny2=cv2.Canny(img2,200,300)
cv2.imshow("edge_detection2",canny2)'''
cv2.waitKey(0)
cv2.destroyAllWindows()