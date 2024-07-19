# Pose Estimation with YOLOv8

This project demonstrates real-time human pose estimation using the YOLOv8 model. It captures video from the webcam, detects human figures, and overlays a skeleton representation of the detected poses.

## Requirements

- Python 3.8 or later
- OpenCV
- Ultralytics YOLO library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aayushjoshi-12/skeleton.git
```
2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

To start the pose estimation, run the `app.py` script:
```bash
python app.py
```

Press `q` to quit the application.

## Files

- `app.py`: The main script that initializes the webcam, performs pose estimation, and displays the results.
- `util.py`: Contains utility functions, including `draw_skeleton` which is used to draw the skeleton on the detected human figures.
- `requirements.txt`: Lists all the Python libraries that need to be installed.
