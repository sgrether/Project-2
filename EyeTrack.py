import FaceDetection
import cv2

def trackEyes(face):
    frame = face.getImage()
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    eyes = eyeCascade.detectMultiScale(frame, 1.7, 5)
    if(len(eyes) == 2): #We didn't find both eyes
        return True
    else:
        return False
