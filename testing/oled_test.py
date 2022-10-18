import machine
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import time

oled = SSD1306_I2C(128, 32, I2C(0,scl=Pin(22), sda=Pin(21)))

oled.fill(0)
oled.invert(False)
oled.contrast(1)
oled.text("Connected",int((128/2)-40),int((32/2)-10))
oled.show()