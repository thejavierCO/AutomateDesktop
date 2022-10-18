# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import network
from ftp import ftpserver
import webrepl_setup
import webrepl
import esp
from env import wifi_name, wifi_pass
esp.osdebug(None)
webrepl.start()

station = network.WLAN(network.STA_IF)
station.active(True)
try:
    station.connect(wifi_name, wifi_pass)
except:
    machine.reset()
while not station.isconnected():
    pass
u = ftpserver()
u.start_thread()
