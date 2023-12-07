# Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

# Read Image and set to Grayscale
img_gray = cv2.cvtColor(cv2.imread('ATU1.jpg'), cv2.COLOR_BGR2GRAY)

# Harris Corner Detection
dst = cv2.cornerHarris(img_gray, 2, 3, 0.04) 

# Deep copy
imgHarris = copy.deepcopy(img_gray)

# Plot cv2 circles on imgHarris
threshold = 0.5; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,( 69, 3, 252 ),-1)


#Plot imgHarris
cv2.imshow("imgHarris",imgHarris)
# cv2.waitKey(0)

# Shi Tomasi Algorithm
corners = cv2.goodFeaturesToTrack(img_gray,100,0.01,10)

# Another Deep copy
imgShiTomasi = copy.deepcopy(img_gray)

# plotting ShiTomasi algorithm corners on image
for i in corners:
    x,y = i.ravel()
    cv2.circle(imgShiTomasi,(int(x),int(y)),3,( 69, 3, 252 ),-1)



#Plot imgShiTomasi
cv2.imshow("imgShiTomasi",imgShiTomasi)
cv2.waitKey(0)

