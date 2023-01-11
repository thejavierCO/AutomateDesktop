from machine import I2C, Pin, reset
from ssd1306 import SSD1306_I2C
from env import wifi_name, wifi_pass
from jco import Numbersbuffer
import time
import uos
import network
try:
    import webrepl
except:
    print("not fount webrepl")
    time.sleep(3)
    reset()

try:
    oled = SSD1306_I2C(128, 32, I2C(0,scl=Pin(22), sda=Pin(21)))
    oled.fill(0)
    oled.invert(True)
    oled.contrast(1)
    oled.show()
    time.sleep(1)
except:
    print("not fount display")

wifi = network.WLAN(network.STA_IF)
if wifi.active() == False:
    wifi.active(True)
    wifi.connect(wifi_name, wifi_pass)
    while wifi.isconnected() == False:
        pass
else:
        print("is connected")
        
webrepl.start()

numbers = Numbersbuffer([
    "0.pbm",
    "1.pbm",
    "2.pbm",
    "3.pbm",
    "4.pbm",
    "5.pbm",
    "6.pbm",
    "7.pbm",
    "8.pbm",
    "9.pbm"
])

if oled:
    oled.invert(False)
    oled.fill(0)
    oled.contrast(1)
    oled.graphic(numbers.Render(str(wifi.ifconfig()[0].split(".")[3])[0],24,32),4*24,0)
    oled.graphic(numbers.Render(str(wifi.ifconfig()[0].split(".")[3])[1],24,32),3*24,0)
    oled.graphic(numbers.Render(str(wifi.ifconfig()[0].split(".")[3])[2],24,32),2*24,0)
    oled.show()
    time.sleep(2)
else:
    print(wifi.ifconfig()[0].split(".")[3])