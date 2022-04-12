import math
import time

import cv2
from djitellopy import tello as drone
from time import sleep
import numpy as np
from Modules import KeyPressModule as kp

####PARAMETRII####
forward_speed = 117/10 #Forward Speed in cm/s (15cm/s)
angular_speed = 360/10 #Angular Speed in degrees/s (50deg/s)
interval = 0.25

distInterval = forward_speed*interval
angInterval = angular_speed*interval
x = 500
y = 500
angle = 0
yaw = 0
######

points = [(0,0),(0,0)]

kp.init()
me = drone.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50

    dist = 0
    global yaw, x, y, angle

    if kp.getKey("LEFT"):
        lr = -speed
        dist = distInterval
        angle = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        dist = -distInterval
        angle = 180

    if kp.getKey("UP"):
        fb = speed
        dist = distInterval
        angle = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        dist = -distInterval
        angle = -90

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"):ud = -speed

    if kp.getKey("a"):
        yv = aspeed
        yaw += angInterval
    elif kp.getKey("d"):
        yv = -aspeed
        yaw -= angInterval

    time.sleep(interval)
    angle+=yaw
    x += int(dist*math.cos(math.radians(angle)))
    y += int(dist * math.sin(math.radians(angle)))

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv, x, y]

def drawPoints(img,points):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0]-500)/100}, {(points[-1][1]-500)/100})m',(points[-1][0]+10,points[-1][1]+30)
                ,cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),1)



while True:
    vals = getKeyboardInput()
    #print(vals)
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])


    img = np.zeros((1000, 1000, 3), np.uint8)
    if(points[-1][0] != vals[4] or points[-1][1] != vals[5]):
        points.append((vals[4], vals[5]))

    drawPoints(img, points)
    cv2.imshow("Map", img)
    cv2.waitKey(1)