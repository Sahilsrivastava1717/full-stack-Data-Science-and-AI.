import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened
if not cap.isOpened():
  print("error")
  exit()

# Define the codec and create VideoWriter object
codec = cv2.VideoWriter_fourcc(*"XVID")
# filename, codec, fps, resolution
recoder = cv2.VideoWriter("output.avi",codec,20.0,(640,480))

while True:
  ret,frame = cap.read()
  if not ret:
   print("failed")
   break
  
  # Write the frame to the output file
  recoder.write(frame)

   # Show the frame
  cv2.imshow("recodinglive",frame)
  
  # Exit on 'q' key press
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release everything
cap.release()
recoder.release()
cv2.destroyAllWindows()
