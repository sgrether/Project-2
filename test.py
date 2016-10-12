#Author Dustin Grady
#Function: Program flow/ user IO
#Status: In progress

import cv2
import FaceDetection
import EyeTrack
import ImageGetter

face = FaceDetection.Face('webcam.jpg')
smile = FaceDetection.findSmile(face)
eyes = EyeTrack.trackEyes(face)

#print(smile)#Testing
#print(eyes)#Testing
key = cv2.waitKey(40) & 0xFF # & 0xFF is for 64-bit support

if(smile == True and eyes == False):
    print('It looks like you were blinking')
    print('Press space to try taking the picture again')
    if key == 32: #Take photo with space bar
        cv.SaveImage("webcam.jpg", cv.fromarray(frame))

if(smile == False and eyes == True):
    print('Why so serious? Try smiling :D')
    print('Press space to try taking the picture again')
    if key == 32: #Take photo with space bar
        cv.SaveImage("webcam.jpg", cv.fromarray(frame))

if(smile == False and eyes == False):
    print('Wake up sleepy face! (No smile or eyes detected)')
    print('Press space to try taking the picture again')
    if key == 32: #Take photo with space bar
        cv.SaveImage("webcam.jpg", cv.fromarray(frame))

if(smile == True and eyes == True):
    print('That looks like a great picture, good work :D')
