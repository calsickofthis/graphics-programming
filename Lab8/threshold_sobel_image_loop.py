import cv2
import numpy as np
import matplotlib.pyplot as plt

def edge_detector(image_path, threshold):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define Sobel filters for horizontal and vertical edges
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Convolve the image with the Sobel filters
    edges_x = cv2.filter2D(img, -1, sobel_x)
    edges_y = cv2.filter2D(img, -1, sobel_y)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(edges_x**2 + edges_y**2)

    # Apply thresholding
    thresholded_image = np.where(gradient_magnitude < threshold, 0, 1)

    plt.imshow(thresholded_image)

    plt.show()

# Visualize results for different thresholds
thresholds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for threshold in thresholds:
    edge_detector('ATU.jpg', threshold)
