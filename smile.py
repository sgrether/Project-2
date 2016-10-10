import cv2

facePath = "/home/gish/CS205_Test/code/haarscascade_frontalface_default.xml"
smilePath = "/home/gish/CS205_Test/code/haarscascade_smile.xml"

faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)
#smileCascade = cv2.CascadeClassifier("haarscascade_frontalface_default.xml")

while(True):
    img = cv2.imread('webcam.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smiles = faceCascade.detectMultiScale(gray, 1.4, 4)
    for (x,y,w,h) in smiles:
        #print(smiles)#Testing
        cv2.rectangle(gray, (x,y), (x+w, y+h), (0,0,0), 2)
    cv2.imshow('img', gray)
    key = cv2.waitKey(1)
    if key == 27: #Exit with escape
        break
cv2.destroyAllWindows()



'''
faces = FACE_CASCADE.detectMultiScale(gray, 1.5, 5)
    for (fx, fy, fw, fh) in faces:
        face = gray[y:fy + fh, x:fx + fw]
        smiles = SMILE_CASCADE.detectMultiScale(face)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face, (sx, sy), (sx+sw, sy+sh), (255, 255, 0), 2)
'''
