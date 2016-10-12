import FaceDetection
import EyeTrack

face = FaceDetection.Face('webcam.jpg')
smile = FaceDetection.findSmile(face)
eyes = EyeTrack.trackEyes(face)
print(smile)
print(eyes)
    
