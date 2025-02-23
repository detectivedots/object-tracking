# Real-Time Object Tracker Using OpenCV

This repository contains a Python implementation for a real-time object tracking system using OpenCV. The system allows a user to select an object from a live webcam feed by drawing a bounding box. The selected object is then tracked in real time using a CSRT tracker.

## Implementation Details

- OpenCV is used for webcam capture and object tracking.
- CSRT tracker is used for real-time object tracking.
- The system uses the 10th frame because during the first frame the camera is a little darker.
- Then `cv2.selectROI` is used to make the user choose an object to track.
- `cv2.TrackerCSRT()` is used to track the object.

## How to run
1. Clone the Repository:
```bash
git clone https://github.com/detectivedots/object-tracking
cd object-tracking
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Run the program:
```bash
python tracker.py
```
