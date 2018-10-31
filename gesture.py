import numpy as np
import cv2

cap = cv2.VideoCapture(0)
Open=np.ones((5,5))
Close=np.ones((20,20))

while(True):
    # capturing the frame
    ret, frame = cap.read()

    # operations for the frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#converting BGR to grey

    #converting the image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower and upper extents of the colors to detect
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #getting only blue images
    blue = cv2.inRange(hsv, lower_blue, upper_blue)

    #operations on the blue object
    blueopen=cv2.morphologyEx(blue, cv2.MORPH_OPEN, Open)
    blueclose=cv2.morphologyEx(blueopen, cv2.MORPH_CLOSE, Close)

    #number of
    _, bluecnts, h = cv2.findContours(blueclose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# if you get too many values to unpack just add _, at the begining

    font=cv2.FONT_HERSHEY_SIMPLEX
    trial=cv2.LINE_AA
    if (len(bluecnts)==0):
        cv2.putText(frame, 'It Fing Works', (0,50), font, 2, (0,255,0), 3, trial)

    elif (len(bluecnts)==1):
        cv2.putText(frame, '1', (0, 50), font, 2, (0, 255, 0), 3, trial)

    elif(len(bluecnts)== 2):
        cv2.putText(frame, '2', (0, 50), font, 2, (0, 255, 0), 3, trial)

    # displaying the frame captured
    cv2.imshow('frame', frame)
    # cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#after running the frame release it
cap.release()
cv2.destroyAllWindows()
