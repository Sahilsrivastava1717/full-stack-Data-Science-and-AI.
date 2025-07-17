import cv2 

# Load the image
image = cv2.imread(r'C:/Users/sahil/OneDrive/Documents/61qbMx4oXJL.jpg')

# Convert the image to grayscale
working_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.resize(image,(100,100))
cv2.resize(working_image,(150,150))

# Get image dimensions for rotation
(h,w) = image.shape[:2]
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,90,1.0)
working_image = cv2.warpAffine(image,M,(w,h))

# Flip the original image in various ways
flip_vertically = cv2.flip(image,0)
flip_horizontally = cv2.flip(image,1)
flip_both = cv2.flip(image,-1)


# Display all images
cv2.imshow("image",image)
cv2.imshow("working_image",working_image)
cv2.imshow("flip_vertically",flip_vertically)
cv2.imshow("flip_horizontally ",flip_horizontally )
cv2.imshow("flip_both",flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows

# Save the original image as a PNG
cv2.imwrite("ouput_python.png",image)
