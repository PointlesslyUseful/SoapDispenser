import numpy as np
import cv2
import glob

face_cascade = cv2.CascadeClassifier('palm.xml')

for file in glob.glob('../training_images/*'):

    img = cv2.imread(file)
    img = cv2.resize(img, (320, 240))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('test.jpg',img)
    cv2.waitKey(0)
