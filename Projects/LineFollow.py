import cv2
import numpy as np
import djitellopy as drone

hsvVals = [0,0,188,179,33,245]#valorile asa incat sa se vada doar drumul
cp = cv2.VideoCapture(0)

me = drone.Tello()
me.connect()
print(me.get_battery())
me.streamon()
#me.takeoff()

thresholdVal=0.2
sensors = 3
width, height = 480,360
sensitivity = 3 #cu cat e mai mare cu atat e mai putin reactiv
weights = [-25,-15,0,15,25]
curba = 0
fSpeed = 15

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsvVals[0],hsvVals[1],hsvVals[2]])
    upper = np.array([hsvVals[3],hsvVals[4],hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)#imaginea cu drumul
    return mask

def getContur(imgThreshold, img):
    contururi, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cx=0
    if len(contururi) != 0:
        mare = max(contururi, key = cv2.contourArea)
        x, y, width, height = cv2.boundingRect(mare)
        cx = x+width//2
        cy = y+height//2

        cv2.drawContours(img, mare, -1, (255,0,255), 7)
        cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)

    return cx

def getSensorOutput(imgThreshold, sensors):
    imgs = np.hsplit(imgThreshold, sensors)
    totalPixels = (img.shape[1]//sensors) * img.shape[0]
    senOut = []
    for x,im in enumerate(imgs):
        pixelCount = cv2.countNonZero(im)
        if pixelCount > thresholdVal * totalPixels:
            senOut.append(1)
        else:
            senOut.append(0)
        #cv2.imshow(str(x),im)
    print(senOut)
    return senOut

def sendCommand(senOut,cx):
    global curba
    ##Translation
    lr = (cx - width//2)//sensitivity
    lr = int(np.clip(lr,-10,10))

    if lr > -2 and lr< 2 :
        lr=0


    ##Rotatia
    if   senOut == [1, 0, 0]:curba = weights[0]
    elif senOut == [1, 1, 0]:curba = weights[1]
    elif senOut == [0, 1, 0]:curba = weights[2]
    elif senOut == [0, 1, 1]:curba = weights[3]
    elif senOut == [0, 0, 1]:curba = weights[4]

    elif senOut == [0, 0, 0]:curba = weights[2]
    elif senOut == [1, 1, 1]:curba = weights[2]
    elif senOut == [1, 0, 1]:curba = weights[2]
    # me.send_rc_control(lr,fSpeed,0,curba)

while True:
    #_, img = cp.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img,(width,height))
    #img = cv2.flip(img,0)

    imgThreshold = thresholding(img)
    cx = getContur(imgThreshold, img) ## For Translation
    senOut=getSensorOutput(imgThreshold, sensors) ## For Rotation
    sendCommand(senOut,cx)

    cv2.imshow("Output",img)
    cv2.imshow("Path", imgThreshold)
    cv2.waitKey(1)