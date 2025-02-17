# Automated Attendance System with Face Recognition

This project is an **Automated Attendance System** that uses **Face Recognition** technology to detect and mark attendance in real time. The system identifies individuals based on their facial features, improving accuracy and ease of use in a classroom or office environment.

## Features:
- **Face Detection**: Detects faces in real-time using the webcam.
- **Face Recognition**: Identifies individuals based on the trained model and marks attendance.
- **Attendance Logging**: Tracks attendance for each individual, recording their name, roll number, and the time of attendance.
- **Real-Time Feedback**: Displays face recognition results on the screen with identified individuals marked with their name.
- **Attendance Report**: Generates and saves daily attendance reports in CSV format.
  
## Requirements:
Before running the project, make sure you have the following Python libraries installed:
- `flask`
- `opencv-python`
- `scikit-learn`
- `joblib`
- `pandas`
- `numpy`
- `SpeechRecognition`
- `pyttsx3`
- `datetime`

You can install the necessary packages using `pip`:
```bash
pip install flask opencv-python scikit-learn joblib pandas numpy SpeechRecognition pyttsx3
