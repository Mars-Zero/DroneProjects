import socket
import cv2

drone_video = cv2.VideoCapture('udp://@0.0.0.0:11111')
while True:
    try:
        ret, frame =drone_video.read()
        if ret:
            cv2.imshow(frame)
            cv2.waitKey(1)
    except Exception as err:
        print(err)

cv2.destroyAllWindows()
drone_video.release()