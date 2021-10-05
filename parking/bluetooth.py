import serial
import re
import numpy as np
ser = serial.Serial('/dev/ttyAMA0', 9600)

def get_bluetooth():
    plate_bl=ser.readline()
    return plate_bl
