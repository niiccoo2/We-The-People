from machine import Pin
from utime import sleep

U = Pin(11, Pin.OUT)
N = Pin(12, Pin.OUT)
I = Pin(5, Pin.OUT)
T = Pin(4, Pin.OUT)
E = Pin(3, Pin.OUT)

U.off()
N.off()
I.off()
T.off()
E.off()



def light_up_sequence():
    U.on()
    sleep(1)
    N.on()
    sleep(1)
    I.on()
    sleep(1)
    T.on()
    sleep(1)
    E.on()
    sleep(1)

def light_off_sequence():
    U.off()
    sleep(1)
    N.off()
    sleep(1)
    I.off()
    sleep(1)
    T.off()
    sleep(1)
    E.off()
    sleep(1)

def blink_sequence():
    for _ in range(4):  # Blink 3 times
        U.off()
        N.off()
        I.off()
        T.off()
        E.off()
        sleep(1)
        U.on()
        N.on()
        I.on()
        T.on()
        E.on()
        sleep(1)

while True:
    light_up_sequence()
    blink_sequence()
    light_off_sequence()
