import sys
import cv2
import numpy as np

# Load video file
cap = cv2.VideoCapture(sys.argv[1])


def detect_lanes(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply gaussian blur to reduce noise (from sides)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Define ROI mask
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array(
        [
            [
                (int(0.1 * width), height),
                (int(0.9 * width), height),
                (int(0.5 * width), int(0.5 * height)),
            ]
        ],
        dtype=np.int32,
    )
    cv2.fillPoly(mask, polygon, 255)

    # Apply the mask to the edges
    masked_edges = cv2.bitwise_and(edges, mask)

    return masked_edges


while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()
    masked_frame = detect_lanes(frame)
    # Display the current frame
    cv2.imshow("tinyslam", masked_frame)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
