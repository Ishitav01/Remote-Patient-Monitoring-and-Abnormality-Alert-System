import cv2
import time
from inactivity_detection import InactivityTracker
from twilio_alerts import AlertManager
from health_suggestions import HealthSuggestion
from pose_detection import PoseDetector

# Initialize components
inactivity_tracker = InactivityTracker(inactivity_threshold=300)  # 5 minutes inactivity threshold
alert_manager = AlertManager()
user_data = {
    "diet_preference": "balanced",
    "inactivity_duration": 0,
    "recent_fall": False
}
health_suggestion = HealthSuggestion(user_data=user_data)
pose_detector = PoseDetector()

# Cooldown period for fall alerts (in seconds)
fall_alert_cooldown = 60  # 1 minute

# Track when the last fall alert was sent
last_fall_alert_time = 0
fall_alert_sent = False  # Track if an alert has been sent

def process_frame(frame):
    global last_fall_alert_time, fall_alert_sent  # Allow modification of global variables

    """
    Process each frame to detect pose, check for inactivity, and trigger alerts if necessary.
    :param frame: The current video frame
    :return: Processed frame with annotations
    """
    motion_status, keypoints = pose_detector.detect_pose(frame)
    print(f"Motion Status: {motion_status}")  # Debug: Track motion status

    if motion_status == "Moving":
        print("Person is moving.")  # Debug
        inactivity_tracker.update_activity(is_moving=True)
        user_data["inactivity_duration"] = 0
        user_data["recent_fall"] = False
        fall_alert_sent = False  # Reset the alert state when moving
    elif motion_status == "Standing":
        print("Person is standing.")  # Debug
        inactivity_tracker.update_activity(is_moving=False)
        user_data["inactivity_duration"] += 1
        user_data["recent_fall"] = False
    elif motion_status == "Fall Detected":
        print("Fall detected!")  # Debug
        inactivity_tracker.update_activity(is_moving=False)
        user_data["inactivity_duration"] += 1
        user_data["recent_fall"] = True

        current_time = time.time()
        if not fall_alert_sent or (current_time - last_fall_alert_time >= fall_alert_cooldown):
            # Send fall alert message using Twilio
            alert_manager.send_sms_alert("Fall detected! Immediate attention required.")
            health_suggestions = health_suggestion.generate_suggestions()
            for suggestion in health_suggestions:
                print(f"Health Suggestion: {suggestion}")

            # Update the time of the last fall alert
            last_fall_alert_time = current_time
            fall_alert_sent = True  # Mark that the alert has been sent

    # Check for prolonged inactivity
    if inactivity_tracker.check_inactivity():
        # Send inactivity alert using Twilio
        alert_manager.send_sms_alert("Prolonged inactivity detected! Please check the user.")
        health_suggestions = health_suggestion.generate_suggestions()
        for suggestion in health_suggestions:
            print(f"Health Suggestion: {suggestion}")
        # Reset inactivity_duration to prevent multiple alerts
        user_data["inactivity_duration"] = 0

    # Display motion status on the frame
    cv2.putText(frame, motion_status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

# Main video processing loop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process the current frame for pose detection, inactivity, and alerts
    processed_frame = process_frame(frame)

    # Display the processed frame
    cv2.imshow('Fall Detection', processed_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
