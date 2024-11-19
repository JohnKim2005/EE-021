import cv2
import numpy as np

# Make sure to store an image called "image.png" in the same directory as this script
# Load the image in grayscale
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# define a filter for the image
image_filter = np.array([[0, 1, 0],
                         [1, -2, 1],
                         [0, 1, 0]])

# Apply the filter to the image using convolution
filtered_image = cv2.filter2D(src=image, ddepth=-1, kernel=image_filter)

# Save the updated image
cv2.imwrite('grayscale_image.png', image)
cv2.imwrite('updated_image.png', filtered_image)