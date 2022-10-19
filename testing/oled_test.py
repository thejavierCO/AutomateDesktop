import machine
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from jco import Numbersbuffer
import time

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

#oled = SSD1306_I2C(128, 32, I2C(0,Pin(22),Pin(21)))

oled.fill(0)
oled.contrast(1)
oled.graphic(numbers.Render(0,24,32),0,0)
oled.show()