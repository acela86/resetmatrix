#!/usr/bin/python

import sys
from time import sleep
from gpiozero import LED

# GPIO definition (for Adafruit RGB Matrix HAT + RTC)
xr1 = LED(5)
xr2 = LED(12)
xg1 = LED(13)
xg2 = LED(16)
xb1 = LED(6)
xb2 = LED(23)

xA = LED(22)
xB = LED(26)
xC = LED(27)
xD = LED(20)

xLAT = LED(21)
xCLK = LED(17)
xOE = LED(4)

# Sending data
# b12  - 1  adds red tinge
# b12  - 9/8/7/6/5  =  4 bit brightness
# b13  - 9   =1 screen on
# b13  - 6   =1 screen off
b12 = 0b0111111111111111
b13 = 0b0000000001000000

def parse_int(s):
    try:
        d = int(s)
    except ValueError:
        return None
    return d

def send_bit(b):
    if (b == 1):
        xr1.on()
        xr2.on()
        xg1.on()
        xg2.on()
        xb1.on()
        xb2.on()
    else:
        xr1.off()
        xr2.off()
        xg1.off()
        xg2.off()
        xb1.off()
        xb2.off()

def send_clk():
    xCLK.on()
    sleep(0.001)

    xCLK.off()
    sleep(0.001)

def get_bit(data, bit):
    return 1 if (data & 2**bit != 0) else 0

def send_cmd(data, width, lat_length):
    for x in range(width):
        y = x % 16
        send_bit(get_bit(data, 15 - y))
        send_clk()

        if (x == (width - lat_length)):
            xLAT.on()

    xLAT.off()

if __name__ == '__main__':
    argv = sys.argv
    if (len(argv) < 2):
        width = 128
    else:
        width = parse_int(argv[1])
        if width is None:
            print('resetmatrix [width]')
            sys.exit()

    print('Matrix width: %d' % width)

    xCLK.off()
    xOE.off()

    xA.on()
    xB.off()
    xC.off()
    xD.off()

    send_bit(0)
    send_cmd(b12, width, 12)
    send_cmd(b13, width, 13)
