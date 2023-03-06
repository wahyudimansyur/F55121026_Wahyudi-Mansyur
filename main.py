import cv2

# Load the two images
img1 = cv2.imread('gambar1.jpeg')
img1 = cv2.resize(img1, (600, 300 ))
img2 = cv2.imread('gambar2.jpeg')
img2 = cv2.resize(img2, (600, 300 ))

# Compute the difference image
diff_img = cv2.absdiff(img1, img2)

# Display the difference image
cv2.imshow('Difference Image', diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
