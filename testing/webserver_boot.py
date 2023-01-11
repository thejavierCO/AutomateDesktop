try:
import gc
import usocket as socket
except:
    import socket

from machine import Pin
from env import wifi_name, wifi_pass
import network

import esp
esp.osdebug(None)

gc.collect()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(wifi_name, wifi_pass)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig()[0])

led = Pin(2, Pin.OUT)
