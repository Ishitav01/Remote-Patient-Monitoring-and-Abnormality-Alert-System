import cv2
import numpy as np
from ultralytics import YOLO

class PoseDetector:
    def __init__(self, model_path='yolov8s-pose.pt', motion_threshold=10, fall_threshold_y=400):
        self.model = YOLO(model_path)  # Load YOLOv8 pose model
        self.prev_keypoints = None
        self.motion_threshold = motion_threshold
        self.fall_threshold_y = fall_threshold_y

    def detect_pose(self, frame):
        """
        Detects pose and motion from the frame using the YOLO model.
        :param frame: Input video frame
        :return: (motion_status, keypoints) where motion_status is "Fall Detected", "Moving", or "Standing"
        """
        frame_resized = cv2.resize(frame, (640, 480))  # Resize frame for faster processing
        results = self.model(frame_resized, device='cpu')  # Run model on CPU

        motion_status = "Unknown"
        keypoints = None

        # Extract pose information
        for r in results:
            if r.keypoints is not None and len(r.keypoints) > 0:
                # Extract keypoints as a numpy array of xy coordinates
                keypoints = r.keypoints[0].xy.cpu().numpy()  # Get keypoints for the first person
                
                # Keypoints: [17, 2] matrix, where each row corresponds to (x, y) coordinates
                y_coordinates = keypoints[:, 1]  # Extract y-coordinates (second column)

                # Fall detection: check if any keypoint's y-coordinate exceeds the threshold
                if np.any(y_coordinates > self.fall_threshold_y):
                    motion_status = "Fall Detected"
                else:
                    if self.prev_keypoints is not None:
                        # Calculate movement by comparing current and previous keypoints
                        movement = np.linalg.norm(keypoints - self.prev_keypoints)
                        motion_status = "Moving" if movement > self.motion_threshold else "Standing"
                
                # Update previous keypoints
                self.prev_keypoints = keypoints

        return motion_status, keypoints
