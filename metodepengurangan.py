import cv2
import numpy as np

# Load the two images
img1 = cv2.imread('daun2.jpg')
img1 = cv2.resize(img1, (400, 500 ))
img2 = cv2.imread('daun.jpg')
img2 = cv2.resize(img2, (400, 500 ))

# Subtract the second image from the first image using NumPy
sub_img = np.subtract(img1, img2)

# Display the original images and the subtracted image
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Subtracted Image", sub_img)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

