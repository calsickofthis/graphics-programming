import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ATU.jpg')
	
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Original image',img)
# cv2.imshow('Gray image', gray)

nrows = 4
ncols = 2

# sobel images
sobelHorizontal = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) # x dir
sobelVertical = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) # y dir

canny = cv2.Canny(img,100,200)


# Original Image
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

# Grayscale Image
plt.subplot(nrows, ncols,2),plt.imshow(gray, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

# GrayScale  & 3*3 Blur
plt.subplot(nrows, ncols,3),plt.imshow(cv2.GaussianBlur(gray,(3, 3),0), cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])

# GrayScale  & 13*13 Blur
plt.subplot(nrows, ncols,4),plt.imshow(cv2.GaussianBlur(gray,(13, 13),0), cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])


# sobelHorizontal
plt.subplot(nrows, ncols,5),plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('sobelHorizontal'), plt.xticks([]), plt.yticks([])

# sobelHorizontal
plt.subplot(nrows, ncols,6),plt.imshow(sobelVertical, cmap = 'gray')
plt.title('sobelVertical'), plt.xticks([]), plt.yticks([])

# sobelSum
plt.subplot(nrows, ncols,7),plt.imshow(sobelHorizontal + sobelVertical, cmap = 'gray')
plt.title('sobel Sum'), plt.xticks([]), plt.yticks([])

# canny
plt.subplot(nrows, ncols,7),plt.imshow(canny, cmap = 'gray')
plt.title('canny'), plt.xticks([]), plt.yticks([])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()