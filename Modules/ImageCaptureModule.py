import djitellopy as drone
import cv2

#image resize script for the drone

me = drone.Tello()
me.connect()
print(me.get_battery())

global img
me.streamon()

def ImageStream():
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Drona", img)
    cv2.waitKey(1)

while True:
    ImageStream()
