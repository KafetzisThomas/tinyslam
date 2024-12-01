#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: tinyslam (https://github.com/KafetzisThomas/tinyslam)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: MIT

import sys
import cv2
import numpy as np

# Load video file
cap = cv2.VideoCapture(sys.argv[1])

# Load haar cascade for vehicle detection
vehicle_cascade = cv2.CascadeClassifier("haarcascade_car.xml")

# Allow window resizing
cv2.namedWindow("tinyslam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("tinyslam", 1100, 700)


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


def edge_detection(blur):
    """
    Perform edge detection.
    """
    edges = cv2.Canny(blur, 50, 150)
    return edges


def region_of_interest(edges):
    """
    Define region of interest (ROI) mask.
    """
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


def hough_transform(masked_edges):
    """
    Detect lines using hough transform.
    """
    lines = cv2.HoughLinesP(
        masked_edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50
    )
    return lines


def detect_vehicles(frame):
    """
    Detect vehicles in the frame.
    """
    gray = grayscale(frame)
    vehicles = vehicle_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    return vehicles


while cap.isOpened():
    # Read next frame
    ret, frame = cap.read()

    gray = grayscale(frame)
    blur = gaussian_blur(gray)
    edges = edge_detection(blur)
    masked_edges = region_of_interest(edges)
    lines = hough_transform(masked_edges)
    vehicles = detect_vehicles(frame)

    # Draw lines
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Draw rectangle around detected vehicles
    for x, y, w, h in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the current frame
    cv2.imshow("tinyslam", frame)

    # Exit loop if key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
