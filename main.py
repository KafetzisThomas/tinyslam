import sys
import cv2

# Load video file
cap = cv2.VideoCapture(sys.argv[1])

while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()
    # Display the current frame
    cv2.imshow("frame", frame)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
