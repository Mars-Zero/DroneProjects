import djitellopy as drone
import time as sleep

#first automation

me = drone.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
#me.move_forward(4)
me.send_rc_control(0,50,0,0)
sleep(2)
me.send_rc_control(50,0,0,0)
sleep(2)
me.send_rc_control(0,0,0,0)
me.land()


