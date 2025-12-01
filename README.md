# Gesture Volume Control

This is an innovative project that allows users to control the volume of their sound devices using simple hand gestures. By utilizing a camera or webcam to capture real-time hand movements, this tool processes the gestures and adjusts the system's volume accordingly, offering a hands-free and intuitive experience.

## Features
- **Real-time Hand Gesture Detection**: Uses machine learning to detect hand gestures through a webcam.
- **Volume Control**: Adjusts the system's volume based on user gestures.
- **User-Friendly**: Easy setup and use without requiring any complex configurations.
  
## Requirements
- Python 3.x (that supports MediaPipe)
- A camera/webcam

## Repository Contents
- **hand_tracker_module.py**: Module that detects hand and finger positions
- **volume_gesture_control.py**: Volume controller

## Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository:
```bash
git clone https://github.com/Fr0st-By7e/Gesture-Volume-Controller.git
```

### 2. Navigate to the project directory:
```bash
cd Gesture-Volume-Controller
```

### 3. Install the required dependencies:
```bash
pip install opencv-python
pip install mediapipe
pip install pycaw
pip install numpy
```

## Usage

1. Connect webcam to your system
2. Run the 'volume_gesture_control.py' file
3. Extend or contract the distance between your index and thumb fingers to change the volume
4. Press 'q' to quit

## How it Works
- The program uses MediaPipe to track the user's hand gestures in real-time using a webcam.
- OpenCV is used for capturing and processing the webcam feed.
- Numpy is used to convert the gesture map to a decibel map
- Pycaw is used to change the volume using the Db map

## Attribution

PyCaw ([github repo URL](https://github.com/AndreMiras/pycaw)) by [Andre Miras], included under the MIT license