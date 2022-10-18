from jco import Led, Btn
from machine import Pin, ADC
import time

btn = Btn(4,True)
led = Led(2,True)
vib = Led(13,True)
time.sleep(1)
led.Write(0)
vib.Write(0)
while True:
    btn.updateTime()
    if btn.Read() == True:
        if btn.timeclick() >= 3:
            led.Write(0)
            vib.Write(1023)
            time.sleep(0.3)
            vib.Write(0)
        elif btn.timeclick() >= 0:
            if led.Read() <= 0:
                led.once_intencidad(1023)
            else:
                led.once_intencidad(led.Read()-int(1023/5))
        time.sleep(0.1)
        continue
    time.sleep(1)
    led.once_reset()