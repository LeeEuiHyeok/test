#-*- coding: utf-8 -*-

import max7219.led as led
import time

device = led.matrix()
s = 0

while True:
    device.pixel(1, 0, s)
    device.pixel(2, 0, s)
    device.pixel(5, 0, s)
    device.pixel(6, 0, s)

    device.pixel(0, 1, s)
    device.pixel(1, 1, s)
    device.pixel(2, 1, s)
    device.pixel(3, 1, s)
    device.pixel(4, 1, s)
    device.pixel(5, 1, s)
    device.pixel(6, 1, s)
    device.pixel(7, 1, s)

    device.pixel(0, 2, s)
    device.pixel(1, 2, s)
    device.pixel(2, 2, s)
    device.pixel(3, 2, s)
    device.pixel(4, 2, s)
    device.pixel(5, 2, s)
    device.pixel(6, 2, s)
    device.pixel(7, 2, s)

    device.pixel(0, 3, s)
    device.pixel(1, 3, s)
    device.pixel(2, 3, s)
    device.pixel(3, 3, s)
    device.pixel(4, 3, s)
    device.pixel(5, 3, s)
    device.pixel(6, 3, s)
    device.pixel(7, 3, s)

    device.pixel(1, 4, s)
    device.pixel(2, 4, s)
    device.pixel(3, 4, s)
    device.pixel(4, 4, s)
    device.pixel(5, 4, s)
    device.pixel(6, 4, s)

    device.pixel(2, 5, s)
    device.pixel(3, 5, s)
    device.pixel(4, 5, s)
    device.pixel(5, 5, s)

    device.pixel(3, 6, s)
    device.pixel(4, 6, s)

    s += 1
    if s == 2:
        s = 0
    time.sleep(0.3)



