from time import sleep
import threading


def timer1():
    print(32322123)
    break


timer = threading.Timer(6.0, timer1)
timer.start()
while True:
    print(1)
    sleep(1)