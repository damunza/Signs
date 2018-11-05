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
    # blue
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #green
    lower_green = np.array([33,100,40])
    upper_green = np.array([100,255,255])

    #red
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])

    #getting only blue images
    blue = cv2.inRange(hsv, lower_blue, upper_blue)

    #getting green object
    green = cv2.inRange(hsv, lower_green, upper_green)

    #getting red object
    red = cv2.inRange(hsv, lower_red, upper_red)

    #operations on the blue object
    blueopen=cv2.morphologyEx(blue, cv2.MORPH_OPEN, Open)
    blueclose=cv2.morphologyEx(blueopen, cv2.MORPH_CLOSE, Close)

    #opperations on the green object
    greenopen=cv2.morphologyEx(green, cv2.MORPH_OPEN, Open)
    greenclose = cv2.morphologyEx(greenopen, cv2.MORPH_CLOSE, Close)

    #opperations on the red object
    redopen = cv2.morphologyEx(red, cv2.MORPH_OPEN, Open)
    redclose = cv2.morphologyEx(redopen, cv2.MORPH_CLOSE, Close)

    #number of blues available
    _, bluecnts, h = cv2.findContours(blueclose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# if you get too many values to unpack just add _, at the begining

    #number of greens available
    _, greencnts, h = cv2.findContours(greenclose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #number of reds available
    _, redcnts, h =cv2.findContours(redclose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    font=cv2.FONT_HERSHEY_SIMPLEX
    trial=cv2.LINE_AA
    if (len(bluecnts)==3):
        #the rectangles for the positions of the blues
        x1, y1, w1, h1 =cv2.boundingRect(bluecnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(bluecnts[1])
        x3, y3, w3, h3 = cv2.boundingRect(bluecnts[2])

        #creating the circles to mark the limits
        cv2.circle(frame, (x1,y1), 20, (0,0,255), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 0, 255), 1)
        cv2.circle(frame, (x3, y3), 20, (0, 0, 255), 1)

        #output for the situation
        cv2.putText(frame, 'F', (0,50), font, 2, (0,255,0), 3, trial)

    elif (len(bluecnts)==4):
        x1, y1, w1, h1 = cv2.boundingRect(bluecnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(bluecnts[1])
        x3, y3, w3, h3 = cv2.boundingRect(bluecnts[2])
        x4, y4, w4, h4 = cv2.boundingRect(bluecnts[3])

        # creating the circles to mark the limits
        cv2.circle(frame, (x1, y1), 20, (0, 0, 255), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 0, 255), 1)
        cv2.circle(frame, (x3, y3), 20, (0, 0, 255), 1)
        cv2.circle(frame, (x4, y4), 20, (0, 0, 255), 1)

        #output for the situation
        cv2.putText(frame, 'B', (0, 50), font, 2, (0, 255, 0), 3, trial)

    elif (len(greencnts)==4):
        x1, y1, w1, h1 = cv2.boundingRect(greencnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(greencnts[1])
        x3, y3, w3, h3 = cv2.boundingRect(greencnts[1])
        x4, y4, w4, h4 = cv2.boundingRect(greencnts[1])

        #making circles
        cv2.circle(frame, (x1, y1), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x3, y3), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x4, y4), 20, (0, 255, 0), 1)

        a = cv2.line(frame, (x1, y1), (x2,y2), (255,0,0),1)
        b = cv2.line(frame, (x2, y2), (x3,y3), (255,0,0),1)
        c = cv2.line(frame, (x3, y3), (x4,y4), (255,0,0),1)

        if len(a)==len(b) & len(b)==len(c) :

            #result
            cv2.putText(frame, 'A', (0, 50), font, 2, (0, 255, 0), 3, trial)

    elif (len(redcnts)==2):
        x1, y1, w1, h1 = cv2.boundingRect(redcnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(redcnts[1])

        cv2.circle(frame, (x1, y1), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 255, 0), 1)

        distance = (((x1-y1)**2) + ((x2-y2)**2))**0.5

        cv2.putText(frame, 'red', (0,50), font, 2, (255, 0, 0), 3, trial)
        
    elif (len(greencnts)==3) & (len(bluecnts)==1):
        x1, y1, w1, h1 = cv2.boundingRect(greencnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(greencnts[1])
        x3, y3, w3, h3 = cv2.boundingRect(greencnts[2])
        x4, y4, w4, h4 = cv2.boundingRect(bluecnts[0])

        cv2.circle(frame, (x1, y1), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x3, y3), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x4, y4), 20, (0, 255, 0), 1)

        # finding the distance between fingers
        distance = (((x3-y3)**2) + ((x4-y4)**2))**0.5

        if distance > 327:
            cv2.putText(frame, 'D', (0,50), font, 2, (255, 0, 0), 3,trial)

    elif (len(greencnts) == 5):
        x1, y1, w1, h1 = cv2.boundingRect(greencnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(greencnts[1])
        x3, y3, w3, h3 = cv2.boundingRect(greencnts[2])
        x4, y4, w4, h4 = cv2.boundingRect(greencnts[3])
        x5, y5, w5, h5 = cv2.boundingRect(greencnts[4])

        cv2.circle(frame, (x1, y1), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x3, y3), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x4, y4), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x5, y5), 20, (0, 255, 0), 1)

        cv2.line(frame, (x1,y1), (x5,y5), (255, 0, 0), 1)

        dist = (((x1-y1)**2) + ((x5-y5)**2))**0.5

        if dist > 148 and dist < 157:
            cv2.putText(frame, 'E', (0,50), font, 2, (255, 0, 0), 3, trial)

        else:
            cv2.putText(frame, '5', (0, 50), font, 2, (255, 0, 0), 3, trial)

    elif (len(greencnts)== 2):
        x1, y1, w1, h1 = cv2.boundingRect(greencnts[0])
        x2, y2, w2, h2 = cv2.boundingRect(greencnts[1])

        cv2.circle(frame, (x1,y1), 20, (0, 255, 0), 1)
        cv2.circle(frame, (x2, y2), 20, (0, 255, 0), 1)

        cv2.putText(frame, 'H', (0, 50), font, 2, (255, 0, 0), 3, trial)

    elif (len(greencnts)== 1):
        x1, y1, w1, h1 = cv2.boundingRect(greencnts[0])

        cv2.circle(frame, (x1,y1), 20, (0, 255, 0), 1)

        cv2.putText(frame, 'G', (0, 50), font, 2, (255, 0, 0), 3, trial)

    # displaying the frame captured
    cv2.imshow('frame', frame)
    # cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#after running the frame release it
cap.release()
cv2.destroyAllWindows()
