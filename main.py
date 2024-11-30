import sys
import cv2

# Load video file
cap = cv2.VideoCapture(sys.argv[1])


def detect_lanes(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply gaussian blur to reduce noise (from sides)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blur, 50, 150)

    return edges


while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()
    edges_frame = detect_lanes(frame)
    # Display the current frame
    cv2.imshow("tinyslam", edges_frame)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
