#Author: Dustin Grady
#Function: Identify smiles within an image

import cv2
import numpy as np
import sys

smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def checkForSmile():
    frame = cv2.imread('webcam.jpg')
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= 1.10,
        minNeighbors=8,
        minSize=(55, 55),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)#Set frame around face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(
        roi_gray,
        scaleFactor = 2.0,
        minNeighbors=22,
        minSize=(25, 25),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        if(len(smile) >= 1): #If there are items in our smiles container
            print(':D')
            return True

        if(len(smile) < 1): #If there are no items in our smiles container
            print('D:')
            return False

#Testing return values
if checkForSmile():
    print('Found smile')
else:
    print('Found frown')
