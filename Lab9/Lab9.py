# Libraries
import cv2
import numpy as np
import matplotlib as plt
import copy

# Read Image and set to Grayscale
img_gray = cv2.cvtColor(cv2.imread('ATU1.jpg'), cv2.COLOR_BGR2GRAY)

# Harris Corner Detection
dst = cv2.cornerHarris(img_gray, 2, 3, 0.04) 

# Deep copy
dc = copy.deepcopy(img_gray)

print(dst)

cv2.imshow("Image",img_gray)
cv2.waitKey(0)