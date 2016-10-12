import numpy as np
import cv2
import time

#cap = cv2.VideoCapture(0)       #640,480
#s, im = cap.read() # captures image

#cv2.imshow("Test Picture", im) # displays captured image
#cv2.imwrite("test.jpg",im) # writes image test.jpg to disk
w = 640
h = 480

def trackEyes():
    #while(cap.isOpened()):
    frame = cv2.imread('webcam.jpg')

    #detect face
    faces = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    detected = faces.detectMultiScale(frame, 1.7, 5)

    #draw square
    for (x,y,w,h) in detected:
        cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,255),1)
        cv2.line(frame, (x,y), ((x+w,y+h)), (0,0,255),1)
        cv2.line(frame, (x+w,y), ((x,y+h)), (0,0,255),1)
      # cv2.rectangle(frame, (x,y),((x+40),(y+40)),(0,0,255),1)
        print(len(detected))
        if(len(detected) == 2): #We didn't find both eyes
            return True
        else:
            return False

if trackEyes():
    print('Not blinking')
else:
    print('Blinking')

#cv2.destroyAllWindows()
