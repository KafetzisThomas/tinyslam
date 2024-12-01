import sys
import cv2

# Load video file
cap = cv2.VideoCapture(sys.argv[1])


def grayscale(frame):
    """
    Convert frame to grayscale.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray


def gaussian_blur(gray):
    """
    Apply gaussian blur to reduce noise (from sides).
    """
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return blur


while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()
    gray = grayscale(frame)
    blur = gaussian_blur(gray)

    # Display the current frame
    cv2.imshow("tinyslam", blur)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()