import FaceDetection

face = FaceDetection.detectFace('webcam.jpg')
smile = FaceDetection.filterSmile(face)
print(smile)
