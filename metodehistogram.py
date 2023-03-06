import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('daun.jpg', 0)

# Calculate the histogram using cv2.calcHist()
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# Display the original and equalized images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[1].imshow(img, cmap='gray')
axs[1].set_title('Equalized Image')
plt.show()

# Plot the histogram using matplotlib
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.show()
