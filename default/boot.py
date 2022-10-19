from machine import I2C, Pin, reset
from ssd1306 import SSD1306_I2C
from env import wifi_name, wifi_pass
import time
try:
    import webrepl
except:
    print("not fount webrepl")
    time.sleep(3)
    reset()
import uos
import network

try:
    oled = SSD1306_I2C(128, 32, I2C(0,scl=Pin(22), sda=Pin(21)))
    oled.fill(0)
    oled.invert(False)
    oled.contrast(1)
    oled.text("start",int((128/2)-40),int((32/2)-10))
    oled.show()
    time.sleep(2)
    oled.fill(0)
except:
    print("not fount display")

station = network.WLAN(network.STA_IF)
if station.active() == False:
    station.active(True)
    station.connect(wifi_name, wifi_pass)
    while station.isconnected() == False:
        pass
else:
        print("is connected")
webrepl.start()