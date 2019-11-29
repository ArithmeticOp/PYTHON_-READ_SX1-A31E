import serial
import time

slaveID = (0x48)
FC = (0x03)
StartAdd_H = (0x00)
StartAdd_L = (0x66)
Register_H = (0x00)
Register_L = (0x01)
CRC_L = (0x6A)
CRC_H = (0x4C)

ser = serial.Serial('/dev/tty.wchusbserial14330',
                    1200, parity=serial.PARITY_EVEN)
print(ser.name)
data = ([slaveID, FC, StartAdd_H, StartAdd_L,
         Register_H, Register_L, CRC_L, CRC_H])
data_bytes = serial.to_bytes(data)

while 1:
    x = ["x[1]", "x[2]", "x[3]", "x[4]", "x[5]", "x[6]", "x[7]", "x[8]"]
    y = ["y[1]", "y[2]", "y[3]", "y[4]", "y[5]", "y[6]", "y[7]", "y[8]"]
    for i in range(1, 8):
        ser.write(data_bytes)
        ser.send_break(0.1)
        time.sleep(0.1)
        x[i] = ser.readline(1)
        y[i] = int.from_bytes(x[i], byteorder='big')
        # print(x[i])
        # print(y[i])
    vol = ((y[4]*256)+y[5])/100
    print(vol)
