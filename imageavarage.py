import cv2
import numpy as np

# Load the images
img1 = cv2.imread('foto1.jpg')
img1 = cv2.resize(img1, (400, 500 ))
img2 = cv2.imread('foto2.jpg')
img2 = cv2.resize(img2, (400, 500 ))

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Compute the average image
avg_img = np.zeros(gray1.shape, dtype=np.float32)
avg_img += gray1.astype(np.float32)
avg_img += gray2.astype(np.float32)
avg_img /= 3.0
avg_img = avg_img.astype(np.uint8)

# Display the original images and the average image
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Average Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
