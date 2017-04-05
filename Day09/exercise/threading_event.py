#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

event = threading.Event()


def light():
    count = 0
    event.set()  # 先设置为绿灯
    while True:
        if count > 5 and count < 10:  # 变为红灯
            event.clear()
            print("\033[1;41mRed light is turned on.\033[0m")
        elif count > 10:
            event.set()  # 变为绿灯
            count = 0
        else:
            print("\033[1;42mGreen light is turned on.\033[0m")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.isSet():
            print("[%s] is running." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light, it's waiting" % name)
            event.wait()
            print("\033[1;34m[%s] sees green light is on, it's keep going." % name)

lights = threading.Thread(target=light)
lights.start()

car1 = threading.Thread(target=car, args=("Jeep",))
car1.start()
