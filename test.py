#Function: Test call to FaceDetection to verify successful implementation of SmileDetector.py

import FaceDetection

face = FaceDetection.detectFace('webcam.jpg')
smile = FaceDetection.filterSmile(face)
print(smile)
