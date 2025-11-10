# This file will be minimal opencv file for mirroring the webcam 

import numpy as np
import cv2 as cv
from playsound import playsound

print('This is mirror.py')


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # turn the image into mirror image 
    frame = cv.flip(frame, 1)
    height, width = frame.shape[:2]

    # play song 
    # playsound("sound.mp3")


    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display text
    cv.putText(frame, 
        "Hello", # Text
        (50,100), # Org
        cv.FONT_HERSHEY_SIMPLEX, #font 
        2, # font Scale
        (100,0,100), #color
        4 #thickness
             )

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()