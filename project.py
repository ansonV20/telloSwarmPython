
import socket
import time
UDP_IP = ["192.168.50.193", "192.168.50.219", "192.168.50.117"]
UDP_PORT = 8889
MESSAGE = ["EXT led 0 255 0", "EXT led 0 255 0", "EXT led 0 255 0"]

from djitellopy import TelloSwarm

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE[0].encode(), (UDP_IP[0], UDP_PORT))
sock.sendto(MESSAGE[1].encode(), (UDP_IP[1], UDP_PORT))
sock.sendto(MESSAGE[2].encode(), (UDP_IP[2], UDP_PORT))

tello1 = "192.168.50.193"
tello2 = "192.168.50.219"
tello3 = "192.168.50.117"

swarm = TelloSwarm.fromIps([
    tello1,
    tello2,
    tello3
])

tello1S = TelloSwarm.fromIps([
    tello1
])
tello2S = TelloSwarm.fromIps([
    tello2
])
tello3S = TelloSwarm.fromIps([
    tello3
])

drone = [tello1S, tello2S, tello3S]
#
swarm.connect()


swarm.takeoff()
swarm.enable_mission_pads()
time.sleep(5)
swarm.move_up(30)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
time.sleep(1)
drone[0].move_up(60)
time.sleep(1)
drone[1].move_up(60)
time.sleep(1)
drone[2].move_up(60)
time.sleep(1)

time.sleep(2)
swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 120, 40, i+1))
swarm.move_up(30)
swarm.move_forward(155)
time.sleep(1)


tello = [tello1,tello2, tello3]
b=0
h = -1
for a in range(3):
    sock.connect((tello[b], UDP_PORT))
    sock.send("tof?".encode())
    data = int(sock.recv(1024)[:-4])/10
    print(data)
    if data <= 100:
        h = b
    b = b + 1
    time.sleep(1)
if h == -1:
    pass
else:
    sock.connect((tello[h], UDP_PORT))
    sock.send("EXT led 255 0 0".encode())

swarm.move_back(145)
time.sleep(1)

swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
# part 2
time.sleep(1)
drone[2].move_down(40)
drone[0].move_up(80)
drone[1].move_up(140)

time.sleep(4)
swarm.parallel(lambda i, tello: tello.go_xyz_speed(20, i * 195 - 195, 0, 100))
drone[2].move_up(100)
drone[1].move_down(90)
swarm.move_down(40)
time.sleep(2)

swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
swarm.move_forward(100)

if h == 0:
    swarm2 = TelloSwarm.fromIps([
        tello2,
        tello3
    ])
elif h == 1:
    swarm2 = TelloSwarm.fromIps([
        tello1,
        tello3
    ])
elif h == 2:
    swarm2 = TelloSwarm.fromIps([
        tello1,
        tello2
    ])
time.sleep(1)
if h == -1:
    swarm.flip_forward()
else:
    drone[h].flip_forward()
    swarm2.flip_forward()


time.sleep(1)
swarm.move_back(110)
swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
swarm.move_down(30)
swarm.move_forward(110)

b=0
h = -1
for a in range(3):
    sock.connect((tello[b], UDP_PORT))
    sock.send("tof?".encode())
    data = int(sock.recv(1024)[:-4])/10
    print(data)
    if data <= 100:
        h = b
    b = b + 1
    time.sleep(1)
if h == -1:
    pass
else:
    sock.connect((tello[h], UDP_PORT))
    sock.send("EXT led 255 0 0".encode())

if h == 0:
    swarm3 = TelloSwarm.fromIps([
        tello2,
        tello3
    ])
elif h == 1:
import socket
import time
UDP_IP = ["192.168.50.193", "192.168.50.219", "192.168.50.117"]
UDP_PORT = 8889
MESSAGE = ["EXT led 0 255 0", "EXT led 0 255 0", "EXT led 0 255 0"]

from djitellopy import TelloSwarm

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE[0].encode(), (UDP_IP[0], UDP_PORT))
sock.sendto(MESSAGE[1].encode(), (UDP_IP[1], UDP_PORT))
sock.sendto(MESSAGE[2].encode(), (UDP_IP[2], UDP_PORT))

tello1 = "192.168.50.193"
tello2 = "192.168.50.219"
tello3 = "192.168.50.117"

swarm = TelloSwarm.fromIps([
    tello1,
    tello2,
    tello3
])

tello1S = TelloSwarm.fromIps([
    tello1
])
tello2S = TelloSwarm.fromIps([
    tello2
])
tello3S = TelloSwarm.fromIps([
    tello3
])

drone = [tello1S, tello2S, tello3S]
#
swarm.connect()


swarm.takeoff()
swarm.enable_mission_pads()
time.sleep(5)
swarm.move_up(30)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
time.sleep(1)
drone[0].move_up(60)
time.sleep(1)
drone[1].move_up(60)
time.sleep(1)
drone[2].move_up(60)
time.sleep(1)

time.sleep(2)
swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 120, 40, i+1))
swarm.move_up(30)
swarm.move_forward(155)
time.sleep(1)


tello = [tello1,tello2, tello3]
b=0
h = -1
for a in range(3):
    sock.connect((tello[b], UDP_PORT))
    sock.send("tof?".encode())
    data = int(sock.recv(1024)[:-4])/10
    print(data)
    if data <= 100:
        h = b
    b = b + 1
    time.sleep(1)
if h == -1:
    pass
else:
    sock.connect((tello[h], UDP_PORT))
    sock.send("EXT led 255 0 0".encode())

swarm.move_back(145)
time.sleep(1)

swarm.parallel(lambda i, tello: tello.go_xyz_speed_mid(0, 0, 100, 40, i+1))
# part 2
time.sleep(1)
drone[2].move_down(40)
drone[0].move_up(80)
drone[1].move_up(140)

time.sleep(4)
swarm.parallel(lambda i, tello: tello.go_xyz_speed(20, i * 195 - 195, 0, 100))
drone[2].move_up(100)
drone[1].move_down(90)
swarm.move_down(40)
time.sleep(2)

swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
swarm.move_forward(100)

if h == 0:
    swarm2 = TelloSwarm.fromIps([
        tello2,
        tello3
    ])
elif h == 1:
    swarm2 = TelloSwarm.fromIps([
        tello1,
        tello3
    ])
elif h == 2:
    swarm2 = TelloSwarm.fromIps([
        tello1,
        tello2
    ])
time.sleep(1)
if h == -1:
    swarm.flip_forward()
else:
    drone[h].flip_forward()
    swarm2.flip_forward()


time.sleep(1)
swarm.move_back(110)
swarm.parallel(lambda i, tello: tello.rotate_clockwise(i%2 * -180 + 180))
swarm.move_down(30)
swarm.move_forward(110)

b=0
h = -1
for a in range(3):
    sock.connect((tello[b], UDP_PORT))
    sock.send("tof?".encode())
    data = int(sock.recv(1024)[:-4])/10
    print(data)
    if data <= 100:
        h = b
    b = b + 1
    time.sleep(1)
if h == -1:
    pass
else:
    sock.connect((tello[h], UDP_PORT))
    sock.send("EXT led 255 0 0".encode())

if h == 0:
    swarm3 = TelloSwarm.fromIps([
        tello2,
        tello3
    ])
elif h == 1:
    swarm3 = TelloSwarm.fromIps([
        tello1,
        tello3
    ])
elif h == 2:
    swarm3 = TelloSwarm.fromIps([
        tello1,
        tello2
    ])

swarm3.move_back(110)

swarm.land()
swarm.end()



    swarm3 = TelloSwarm.fromIps([
        tello1,
        tello3
    ])
elif h == 2:
    swarm3 = TelloSwarm.fromIps([
        tello1,
        tello2
    ])

swarm3.move_back(110)

swarm.land()
swarm.end()


