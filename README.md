# tinyslam

**What is this?**  
A minimalist implementation of monocular SLAM, inspired by [twitchslam](https://github.com/geohot/twitchslam). Created as a learning project to understand the basics of SLAM.

## Usage

```bash
$ pip3 install -r requirements.txt
$ python3 main.py < video_file.mp4 >
```

## How It Works

The process is broken into clear modular steps:

1. **[Load video file](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/load_video.py):** Reads the input video for processing.
2. **[Grayscale conversion](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/grayscale.py):** Converts the frames to grayscale to simplify processing.
3. **[Gaussian blur](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/gaussian_blur.py):** Reduces noise for better edge detection.
4. **[Edge detection](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/edge_detection.py):** Detects edges in the blurred frames.
5. **[Region of interest (ROI) extraction](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/region_of_interest.py):** Focuses on the region where lanes are expected.
6. **[Hough transform for line detection](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/hough_transform.py):** Detects lane lines in the ROI.
7. **[Haar cascade for vehicle detection](https://github.com/KafetzisThomas/tinyslam/blob/main/tests/haar_cascade.py):** Detects vehicles in the frame (gray frame).

## Demo Videos

### Lane Lines Detection
https://github.com/user-attachments/assets/5e9a44cc-22ae-49e9-bcfd-f71e85fad728

### Lane Lines + Vehicle Detection
https://github.com/user-attachments/assets/cd67fb2a-a3ce-4104-bac4-139f1e966fbf
