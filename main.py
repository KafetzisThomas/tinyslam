import sys
import cv2
import numpy as np

# Load video file
cap = cv2.VideoCapture(sys.argv[1])


def grayscale(frame):
    """
    Convert frame to grayscale.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray


def detect_lanes(frame):
    gray = grayscale(frame)

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

    # Detect lines using hough transform
    lines = cv2.HoughLinesP(
        masked_edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50
    )

    return lines


while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()
    lines = detect_lanes(frame)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Display the current frame
    cv2.imshow("tinyslam", frame)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
