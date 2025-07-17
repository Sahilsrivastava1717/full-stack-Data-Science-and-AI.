import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Video", frame)  # Show the frame

    # Break loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
