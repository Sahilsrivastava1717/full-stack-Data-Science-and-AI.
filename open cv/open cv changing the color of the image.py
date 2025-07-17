import cv2

location = input("enter the loc:")
image = cv2.imread(location)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


cv2.imshow("Open Photo", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
cv2.imwrite("output_python.jpg", image)

