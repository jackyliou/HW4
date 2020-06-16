import matplotlib.pyplot as plt
import numpy as np
import serial
import time

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())
s.write("ATMY 0x128\r\n".encode())
char = s.read(3)
print("Set MY 0x128.")
print(char.decode())
s.write("ATDL 0x228\r\n".encode())
char = s.read(3)
print("Set DL 0x228.")
print(char.decode())
s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())
s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())
s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())
s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())
s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
i = 0
t = np.arange(0,20,1)
num = np.arange(0,20,1) 
while True:
    # send RPC to remote
    s.write("/ACC/run\r".encode())
    print("sent RPC!")

    char = s.read(1)
    de_ch= char.decode()
    if de_ch !='\r':
        ch1 = de_ch
        char = s.read(1)
        ch2= char.decode()
        num[i] = int(ch1+ch2)
        i = i + 1
        print(num)
    time.sleep(1)
    if i == 20:
        break
print("start plot!")
# output fig
fig, ax = plt.subplots(1, 1)

ax.plot(t,num)
ax.set_xlabel('Timestep')
ax.set_ylabel('number')
plt.show()

s.close()