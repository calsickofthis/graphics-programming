import cv2
import numpy as np
import matplotlib.pyplot as plt

def edge_detector(image_path):
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

    # Display the results
    plt.figure(figsize=(10, 5))

    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.axis('off')

    plt.subplot(132), plt.imshow(edges_x, cmap='gray')
    plt.title('Horizontal Edges'), plt.axis('off')

    plt.subplot(133), plt.imshow(edges_y, cmap='gray')
    plt.title('Vertical Edges'), plt.axis('off')

    plt.show()

    # Display the gradient magnitude
    plt.figure(figsize=(5, 5))
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Gradient Magnitude'), plt.axis('off')
    plt.show()

# Example usage
edge_detector('ATU.jpg')
