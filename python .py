import serial
import time
ser = serial.Serial('COM3', 9600, timeout=1)
while(True):
        cX = input ("enter your command: \n")
        ser.write(bytes(str(cX),'utf8'))
ser.close()
