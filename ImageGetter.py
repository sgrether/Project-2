#Author: Dustin Grady
#Function: Takes pictures using webcam when the space bar is pressed and saves them to the directory for processing by other function
#Status: Finished/ Working
#Github: https://github.com/sgrether/Project-2/tree/D-Features

import cv2
import cv

def getImage():
    cv2.namedWindow("Space to capture | Esc to analyze")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    print "\n\n\n\n\nTaking photo.."

    while rval:
        cv2.imshow("Space to capture | Esc to analyze", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(40) & 0xFF # & 0xFF is for 64-bit support
        if key == 27: #esc to exit
            break

        if key == 32: #Take photo with space bar
            cv.SaveImage("webcam.jpg", cv.fromarray(frame))
getImage()
