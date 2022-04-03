import djitellopy as drone
import time as sleep

me = drone.Tello()
me.connect()
print(me.get_battery())