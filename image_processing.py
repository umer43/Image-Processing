import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg')  # Replace with your image path

# Convert the image from BGR (OpenCV default) to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original image
plt.imshow(image_rgb)
plt.axis('off')  # Hide axes
plt.show()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the edges
plt.imshow(edges, cmap='gray')
plt.axis('off')
plt.show()

# Save the processed images
cv2.imwrite('grayscale_image.jpg', gray_image)
cv2.imwrite('edges_image.jpg', edges)
