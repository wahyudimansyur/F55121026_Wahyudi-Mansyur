import cv2
import numpy as np

# Load the image
img = cv2.imread('anjing.jpg')

# Set the kernel size (filter size)
kernel_size = (5, 5)

# Create the kernel (filter)
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# Apply the filter using cv2.filter2D() function
output = cv2.filter2D(img, -2, kernel)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', output)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
