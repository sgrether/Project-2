import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)       #640,480
s, im = cap.read() # captures image
cv2.imshow("Test Picture", im) # displays captured image
cv2.imwrite("test.jpg",im) # writes image test.jpg to disk
w = 640
h = 480

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        #detect face
        faces = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        detected = faces.detectMultiScale(frame, 1.3, 5)

        #draw square
        for (x,y,w,h) in detected:
                cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,255),1)
                cv2.line(frame, (x,y), ((x+w,y+h)), (0,0,255),1)
                cv2.line(frame, (x+w,y), ((x,y+h)), (0,0,255),1)
              # cv2.rectangle(frame, (x,y),((x+40),(y+40)),(0,0,255),1)        


        #show picture
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
