from docx import Document
from docx.shared import Inches, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Create a new Word Document
doc = Document()

# Set the style for the document
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(11)

# Create a table with 7 columns (headers) and 14 rows (1 header + 13 papers)
table = doc.add_table(rows=1, cols=7)
table.style = 'Table Grid'

# Set column headers
headers = [
    "Paper No.", "Year", "Research Focus", "Methodology",
    "Key Findings", "Gaps Identified", "Scope Research for Future"
]
hdr_cells = table.rows[0].cells
for i, header in enumerate(headers):
    hdr_cells[i].text = header

# Data rows (rows 1 to 13)
rows = [
    ["Paper 1", "2019", "Pose Detection for Patient Monitoring (Malasinghe et al., 2019)",
     "Pose detection algorithms, AI techniques",
     "Highlights the potential of pose detection to enhance patient monitoring and alert systems.",
     "Limited exploration of different patient conditions and poses; real-time data handling improvements needed.",
     "Expanding real-time pose detection across diverse healthcare settings and patient demographics."],

    ["Paper 2", "2020", "CNN-Based Human Activity Recognition for Healthcare (Gul et al., 2020)",
     "Convolutional Neural Networks (CNN), image processing",
     "Demonstrates CNN effectiveness in identifying human activities, enhancing patient monitoring.",
     "Limited activity diversity in datasets; lacks real-world clinical testing.",
     "Broaden dataset variety and validate model performance in real clinical environments."],

    ["Paper 3", "2023", "Automated Real-Time Patient Monitoring Alert System (Shaik et al., 2023)",
     "Alert systems, AI, real-time data processing",
     "Shows automated alert systems improve patient safety and monitoring efficiency.",
     "Insufficient scalability and alert accuracy; limited testing across healthcare settings.",
     "Developing scalable systems and testing alert accuracy across various healthcare environments."],

    ["Paper 4", "2023", "Secure WebCam Pose-Based Health Monitoring and Abnormality Alert System (Whitehead1 & Conley, 2023)",
     "Webcam technology, AI algorithms, alert systems",
     "Emphasizes non-invasive monitoring’s role in timely patient care interventions.",
     "Privacy concerns with video data; performance issues in low-light or complex environments.",
     "Address privacy and optimize for low-light settings in various monitoring conditions."],

    ["Paper 5", "2024", "Patient Monitoring by Abnormal Human Activity Recognition Based on CNN Architecture (Rahman et al., 2024)",
     "CNN, abnormal activity recognition",
     "Highlights CNN’s capability to alert caregivers to abnormal activities, improving patient safety.",
     "Limited abnormal activity datasets; generalization needed for diverse populations.",
     "Expand datasets to represent diverse demographics and refine algorithms for broader applicability."],

    ["Paper 6", "2021", "Remote Patient Monitoring Using AI: Applications and Challenges (Yadav et al., 2021)",
     "AI, IoT, cloud computing, blockchain",
     "Concludes AI-enabled RPM enhances monitoring but faces data privacy and learning challenges.",
     "Data privacy, explainability, and adaptability issues in RPM; IoMT device integration.",
     "Enhance privacy measures and integration of IoMT devices for secure and effective RPM solutions."],

    ["Paper 7", "2024", "YOLO for Medical Object Detection: A Systematic Review (Ragab et al., 2024)",
     "Systematic review of YOLO on PubMed studies (2018-2023)",
     "YOLO outperforms traditional methods but faces high computational demands and dataset limitations.",
     "High computational requirements; challenges detecting small/occluded objects.",
     "Develop lightweight YOLO variants and address annotation limitations in medical imaging datasets."],

    ["Paper 8", "2021", "Efficient Deep Learning Model for Human Activity Recognition Using Smartphones (Ankita et al., 2021)",
     "CNN-LSTM model with UCI-HAR dataset",
     "Achieved high accuracy; model demonstrated robustness for lightweight applications.",
     "Limited sensor combination exploration; issues with generalization to other devices.",
     "Investigate sensor fusion techniques and test across varied wearable devices for broader applicability."],

    ["Paper 9", "2024", "YOLO Models for Detection of People with Disabilities (Alruwaili et al., 2024)",
     "YOLOv8, YOLOv7, YOLOv5",
     "YOLOv8 achieved superior precision; detected visible mobility aids effectively.",
     "Limited detection for subtle disabilities; lacks depth and posture estimation.",
     "Enhance detection for hidden disabilities and integrate depth estimation for more comprehensive monitoring."],

    ["Paper 10", "2024", "Real-Time Fire Surveillance and Alert Integration with Twilio (Imogen et al., 2024)",
     "YOLOv8, MobileNet CNN, Twilio",
     "Achieved 97.1% accuracy in fire detection; integration proposed with predictive analytics.",
     "Limited testing across environments; lacks predictive pre-emptive alert capabilities.",
     "Expand testing conditions and integrate predictive analytics for proactive fire detection."],

    ["Paper 11", "2019", "Blockchain-based Management of Video Surveillance Systems (Jeong et al., 2019)",
     "Blockchain, IPFS, Chaincode API",
     "Achieved secure video data management, preventing unauthorized access and ensuring integrity.",
     "Scalability and interoperability challenges in current blockchain frameworks.",
     "Improve blockchain scalability and interoperability for more robust video data management."],

    ["Paper 12", "2024", "Consortium Blockchain for Reliable Remote Health Monitoring (Upadrista et al., 2024)",
     "Consortium blockchain, smart contracts, Elasticsearch",
     "Enhanced data availability and integrity, enabling multi-hospital integration.",
     "Need for better interoperability among healthcare networks; single-point failure (SPoF) in blockchain.",
     "Develop interoperable systems among healthcare networks and address SPoF to enhance data reliability."],

    ["Paper 13", "2020", "Health 4.0: Realizing the Healthcare of the Future (Al-Jaroodi et al., 2020)",
     "Service-oriented middleware (SOM), IoT, big data",
     "Health 4.0 improves flexibility, scalability, and quality in healthcare services.",
     "Security, privacy, and ethical challenges with diverse technology integration.",
     "Explore secure and privacy-focused Health 4.0 solutions for collaborative, tech-enabled healthcare systems."]
]

# Add data to the table
for row in rows:
    cells = table.add_row().cells
    for i, item in enumerate(row):
        cells[i].text = item

# Save the document
file_path = "C:\Users\ishus\Desktop\Research Paper\Required data graphs\Table\table.docx"
doc.save(file_path)

file_path
