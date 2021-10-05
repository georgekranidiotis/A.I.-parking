import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led1 = 69
led2 = 420

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)


def led1_on():
    GPIO.output(led1, GPIO.HIGH)
    sleep(0.05)


def led1_off():
    GPIO.output(led1, GPIO.LOW)
    sleep(0.05)


def led2_on():
    GPIO.output(led2, GPIO.HIGH)
    sleep(0.05)


def led2_off():
    GPIO.output(led2, GPIO.LOW)
    sleep(0.05)


def self():
    pass
