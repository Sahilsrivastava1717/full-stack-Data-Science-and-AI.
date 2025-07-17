import cv2

# Read the image from file
image = cv2.imread(r"C:\Users\sahil\OneDrive\Documents\61qbMx4oXJL.jpg")

# Resize the image to 400x300 pixels
resize = cv2.resize(image,(400,300))

# Display the original image
cv2.imshow('image showing',image)

# Display the resized image
cv2.imshow('resized image',resize)
cv2.waitKey(0)
cv2.destroyAllWindows


# Save the original image to file
cv2.imwrite("output_python.jpg", image)

