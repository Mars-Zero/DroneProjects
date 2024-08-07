import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
drone_address = ('192.168.10.1',8889)
sock.bind(('',9000))

while True:
    try:
        msg= input('')
        if not msg:
            break
        if 'end' in msg:
            sock.close()
            break
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg,drone_address)
    except Exception as err:
        print(err)
        sock.close()
        break