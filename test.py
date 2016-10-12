import FaceDetection

face = FaceDetection.Face('webcam.jpg')
smile = FaceDetection.findSmile(face)
print(smile)
