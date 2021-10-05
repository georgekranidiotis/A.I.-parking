from datetime import time
from url import send_plate
from find_plate_ra import find_pl_ra
from sort import find_more
from bluetooth import get_bluetooth
from rfid import get_rfid
from is_plate import is_plate
from shapes import time_elapsed, zero_screen, show_plate, code_sent
import threading
from leds import led1_on, led1_off, led2_on, led2_off

joe = []
plate = ""
plate_bl = ""
plate_rf = ""
rg = ""
bk = ""
send = True
cert = ""


def timer1():
    bk, cert = send_plate(plate)
    time_elapsed(bk)
    bk = ""
    send = False
    if cert == "yes":
        led1_off()
    else:
        led2_on()


timer = threading.Timer(60, timer1)

while True:
    joe = find_pl()
    plate = find_more(joe)
    if is_plate(plate):
        timer.start()
        start_time = time.time
        show_plate(plate)
        led1_on()
        while find_more(find_pl()) == plate:
            plate_bl = get_bluetooth()
            plate_rf = get_rfid()
            if send:
                if plate_rf != "":
                    timer.cancel()
                    rg, cert = send_plate(plate_rf)
                    code_sent(rg)
                    send = False
                    if cert == "yes":
                        led1_off()
                    else:
                        led2_on()
                elif plate_bl != "":
                    timer.cancel()
                    rg, cert = send_plate(plate_bl)
                    code_sent(rg)
                    send = False
                    if cert == "yes":
                        led1_off()
                    else:
                        led2_on()
        zero_screen()
        plate = ""
        plate_bl = ""
        plate_rf = ""
        rg = ""
        send = True
        led1_off()
        led2_off()
