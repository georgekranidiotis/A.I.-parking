import serial
import re
import numpy as np
ser = serial.Serial('/dev/ttyACM0', 9600)
sl=''
f=''
def get_rfid():
    a=ser.readline()
    sl = str(a[0:len(a) - 2].decode("utf-8"))
    if a ='t':
        f=ser.readline()
        plate_rf = str(a[0:len(a) - 2].decode("utf-8"))
        return plate_rf