from djitellopy import tello as drone
from time import time
import cv2
from Modules import KeyPressModule as kp
from Modules import ImageCaptureModule as im

#keyboard support for the drone

kp.init()
me = drone.Tello()
me.connect()
print(me.get_battery())


me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed=50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"):ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',im.img)
        time.sleep(0.3)#poate schimb asta

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    #print(vals)
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    im.ImageStream()