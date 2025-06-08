import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLOv8 model
yolo_model = YOLO('models/yolov8n-pose.pt')  # Update this path to your YOLO model file

# Function to infer pose from keypoints
def infer_pose_from_keypoints(keypoints):
    """
    Infers the pose based on keypoint y-coordinates and relative positions.
    """
    if len(keypoints) == 0:
        return "No Pose Detected"

    # Example heuristic rules based on keypoint positions
    head_y = keypoints[0][1]  # Nose (y-coordinate)
    hip_y = keypoints[11][1]  # Left hip (y-coordinate)
    knee_y = keypoints[13][1]  # Left knee (y-coordinate)

    if abs(head_y - hip_y) < 50:  # Threshold for "bending" (head close to hip)
        return "Bending"
    elif hip_y < knee_y:  # If hip is higher than knees
        return "Standing"
    else:
        return "Falling"

# Function to process a single image
def process_single_image(image_path, output_path='output_image.jpg'):
    # Load the image
    image = cv2.imread('20220709_123733(0).jpg')
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # Perform pose detection with YOLOv8
    results = yolo_model(image)
    result = results[0]

    # Extract keypoints for the first person detected
    keypoints = result.keypoints.cpu().numpy() if result.keypoints is not None else np.array([])

    if len(keypoints) > 0:
        keypoints = keypoints[0]  # Use the first detected person's keypoints
        pose = infer_pose_from_keypoints(keypoints)
    else:
        pose = "No person detected"

    # Annotate the image with the detected pose
    annotated_image = result.plot()  # YOLOv8 function to overlay keypoints
    cv2.putText(annotated_image, f"Pose: {pose}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Save the annotated image
    cv2.imwrite(output_path, annotated_image)
    print(f"Processed image saved as '{output_path}' with detected pose: {pose}")

# Example usage
if __name__ == "__main__":
    # Input and output paths
    input_image_path = 'input_image.jpg'  # Replace with the path to your input image
    output_image_path = 'output_image.jpg'  # Output path for the processed image

    # Process the image
    process_single_image(input_image_path, output_image_path)
