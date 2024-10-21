import cv2
import torch
import math
import pandas
import requests

# Load the YOLOv5 Nano model
model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

def get_front_data():
    print("Capturing front data from stereo camera...")
    frame1 = get_front_data_1()  # Capture from the left lens
    frame2 = get_front_data_2()  # Capture from the right lens

    # Perform inference on both frames
    detect_objects(frame1, "Camera 1")
    detect_objects(frame2, "Camera 2")

def get_front_data_1():
    print("Capturing front data from camera 1...")
    return capture_data(0)  # Assuming camera 1 is at index 0

def get_front_data_2():
    print("Capturing front data from camera 2...")
    return capture_data(1)  # Assuming camera 2 is at index 1

def get_back_data():
    print("Capturing back data...")
    frame = capture_data(2)  # Assuming back camera is at index 2
    detect_objects(frame, "Back Camera")

def get_left_data():
    print("Capturing left data...")
    frame = capture_data(3)  # Assuming left camera is at index 3
    detect_objects(frame, "Left Camera")

def get_right_data():
    print("Capturing right data...")
    frame = capture_data(4)  # Assuming right camera is at index 4
    detect_objects(frame, "Right Camera")

def capture_data(camera_index):
    # Initialize video capture
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Error: Camera at index {camera_index} could not be opened.")
        return None

    # Capture a single frame
    ret, frame = cap.read()
    if ret:
        # Show the captured frame.
        #uncomment for headful env # cv2.imshow(f"Camera {camera_index}", frame)
        #uncomment for headful env # cv2.waitKey(1)  # Short wait to display the frame
        return frame  # Return the captured frame for further processing
    else:
        print(f"Error: Failed to capture image from camera {camera_index}.")
        return None

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

def detect_objects(frame, camera_name):
    if frame is not None:
        # Perform inference
        results = model(frame)

        # Print results
        print(f"Detection results from {camera_name}:")
        results.print()  # Print results to console
        results.show()   # Show results in a window

        # Save or process results as needed
        # e.g., results.save() to save detections to disk

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

