# Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

# rows and columns for subplot
nrows = 4
ncols = 2

# Read Image and set to Grayscale
# img_gray = cv2.cvtColor(cv2.imread('ATU1.jpg'), cv2.COLOR_BGR2GRAY)
img_gray = cv2.cvtColor(cv2.imread('monaghan.jpg'), cv2.COLOR_BGR2GRAY)

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

# Shi Tomasi Algorithm
corners = cv2.goodFeaturesToTrack(img_gray,100,0.01,10)

# Another Deep copy
imgShiTomasi = copy.deepcopy(img_gray)

# plotting ShiTomasi algorithm corners on image
for i in corners:
    x,y = i.ravel()
    cv2.circle(imgShiTomasi,(int(x),int(y)),3,( 69, 3, 252 ),-1)

# Using ORB to detect key features - Initiate ORB detector - find keypoints - compute the descriptors and draw the keypoits on image
# from https://docs.opencv.org/4.x/d1/d89/tutorial_py_orb.html
orb = cv2.ORB_create()
kp = orb.detect(img_gray,None)
kp, des = orb.compute(img_gray, kp)
img2 = cv2.drawKeypoints(img_gray, kp, None, color=(0,255,0), flags=0)


# imgHarris
plt.subplot(nrows, ncols,1),plt.imshow(imgHarris, cmap = 'gray')
plt.title('imgHarris'), plt.xticks([]), plt.yticks([])

# ORB Image
plt.subplot(nrows, ncols,2),plt.imshow(img2, cmap = 'gray')
plt.title('ORB computed keypoints'), plt.xticks([]), plt.yticks([])

# imgShiTomasi
plt.subplot(nrows, ncols,3),plt.imshow(imgShiTomasi, cmap = 'gray')
plt.title('imgShiTomasi'), plt.xticks([]), plt.yticks([])

plt.show()


# Feature Matching
img1 = cv2.imread('monaghan.jpg',cv2.IMREAD_GRAYSCALE)# queryImage
img2 = cv2.imread('Monaghan Courthouse.jpg',cv2.IMREAD_GRAYSCALE) # trainImage
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('comparison',img3)

# rows and columns for subplot
nrows = 4
ncols = 2

# mig = cv2.cvtColor(cv2.imread('ATU1.jpg'), cv2.COLOR_BGR2RGB)
mig = cv2.imread('ATU2.jpg')

# split the channels
b,g,r = cv2.split(mig)

# Blue Channel
plt.subplot(nrows, ncols,1),plt.imshow(b)
plt.title('Blue Channel'), plt.xticks([]), plt.yticks([])

# Green Channel
plt.subplot(nrows, ncols,2),plt.imshow(g)
plt.title('Green Channel'), plt.xticks([]), plt.yticks([])

# Red Channel
plt.subplot(nrows, ncols,3),plt.imshow(r)
plt.title('Red Channel'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)