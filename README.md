# Remote Patient Monitoring and Abnormality Alert System
  Real-time Fall Detection and Health Monitoring System using YOLOv8, CNN, Twilio, and Firebase. Detects human poses through webcam, classifies activities (e.g., standing, sitting, falling), sends instant alerts via SMS, and provides health suggestions — ideal for elderly and post-surgery patient monitoring.

# 🛡️ Fall Detection and Health Monitoring System

A secure, real-time **pose-based health monitoring** and **fall detection system** using **YOLOv8**, **CNN**, **Twilio**, and **Firebase**. Designed for remote monitoring of elderly or post-surgery patients, the system provides **real-time alerts**, **activity recognition**, and **personalized health suggestions**.

---

## 🚀 Features

- 🔍 Real-time pose detection using YOLOv8
- 🧠 Activity classification: standing, walking, sitting, falling
- ⚠️ Fall & inactivity detection logic
- 📩 SMS alerts to caregivers using Twilio
- 🩺 Personalized health suggestions
- ☁️ Firebase for real-time data storage
- 🔒 Optional blockchain-based alert logging

---

## 🧠 Technologies Used

| Component         | Technology             |
|------------------|------------------------|
| Pose Detection   | YOLOv8 (Ultralytics)   |
| Pose Classification | CNN (TensorFlow / PyTorch) |
| Alerting         | Twilio API             |
| Data Storage     | Firebase (NoSQL)       |
| GUI (optional)   | Tkinter / Streamlit    |
| Blockchain (optional) | Web3 / Simulated   |
| Video Handling   | OpenCV                 |
| Language         | Python 3.x             |

---

## 📁 Project Structure

```bash
.
├── main.py                # Main system pipeline
├── pose_detection.py      # YOLOv8 pose detection module
├── inactivity_detection.py # Detects prolonged inactivity
├── twilio_alerts.py       # Sends alerts via SMS
├── health_suggestions.py  # Suggests health tips based on user state
├── mainimage.py           # Pose detection on single image
├── requirements.txt       # List of required Python libraries
├── .env                   # Environment variables (Twilio keys)
├── fall.mp4               # Sample test video
├── yolov8s-pose.pt        # Pretrained YOLOv8 pose model
└── README.md              # Project documentation


📦 Installation
1. Clone the Repository
git clone https://github.com/your-username/fall-detection-system.git
cd fall-detection-system

2. Create Virtual Environment
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

3. Install Requirements
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the root directory:
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=your_twilio_number
TARGET_PHONE_NUMBER=recipient_number

▶️ Run Full System
python main.py

🖼️ Test on Image
python mainimage.py --image path/to/image.jpg

📩 Send Test SMS
python twilio_alerts.py

🗃️ Datasets Used
UR Fall Detection Dataset

UP-Fall Detection Dataset

COCO Keypoints

MPII Human Pose

📈 Results
| Metric                  | Value    |
| ----------------------- | -------- |
| Pose Detection Accuracy | 94.5%    |
| Fall Detection Accuracy | 94.37%   |
| Inactivity Accuracy     | 92.9%    |
| Avg. Processing Latency | 180 ms   |
| SMS Alert Delay         | < 100 ms |

🧩 System Architecture
Camera Input
     ↓
YOLOv8 Pose Detection → CNN Pose Classification
     ↓
Inactivity / Fall Detection Logic
     ↓
Twilio SMS Alert + Firebase Logging
     ↓
Health Suggestion Generator

📜 Research Paper
The detailed research paper explaining the architecture, models, accuracy comparison, and evaluation is available in the  IEEE Conference.

📬 Contact
GitHub: @Ishitav01
Email: ishusomani02@gmail.com

📄 License
This project is open-source and available under the MIT License.



