from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import framebuf
import math
import time

oled = SSD1306_I2C(128, 32, I2C(0,scl=Pin(22), sda=Pin(21)))
lista = ["0.pbm","1.pbm","2.pbm","3.pbm","4.pbm","5.pbm","6.pbm","7.pbm","8.pbm","9.pbm"]
numberBuffer = []
for archivo in lista:
    with open(archivo,"rb") as f:
        f.readline()
        f.readline()
        numberBuffer.append(bytearray(f.read()))
    f.close()
def printNumber(number,posy=0,posx=0):
    w=24
    h=32
    fbuf = framebuf.FrameBuffer(numberBuffer[0],w,h,framebuf.MONO_HLSB)
    if number == 1:
        fbuf = framebuf.FrameBuffer(numberBuffer[1],w,h,framebuf.MONO_HLSB)
    if number == 2:
        fbuf = framebuf.FrameBuffer(numberBuffer[2],w,h,framebuf.MONO_HLSB)
    if number == 3:
        fbuf = framebuf.FrameBuffer(numberBuffer[3],w,h,framebuf.MONO_HLSB)
    if number == 4:
        fbuf = framebuf.FrameBuffer(numberBuffer[4],w,h,framebuf.MONO_HLSB)
    if number == 5:
        fbuf = framebuf.FrameBuffer(numberBuffer[5],w,h,framebuf.MONO_HLSB)
    if number == 6:
        fbuf = framebuf.FrameBuffer(numberBuffer[6],w,h,framebuf.MONO_HLSB)
    if number == 7:
        fbuf = framebuf.FrameBuffer(numberBuffer[7],w,h,framebuf.MONO_HLSB)
    if number == 8:
        fbuf = framebuf.FrameBuffer(numberBuffer[8],w,h,framebuf.MONO_HLSB)
    if number == 9:
        fbuf = framebuf.FrameBuffer(numberBuffer[9],w,h,framebuf.MONO_HLSB)
    oled.framebuf.blit(fbuf,int(posy*w),int(posx*h))
while True:
    oled.fill(0)
    printNumber(4,0,0);
    printNumber(3,1,0);
    printNumber(2,2,0);
    printNumber(1,3,0);
    oled.show()
    time.sleep(3)
    oled.fill(0)
    printNumber(8,0,0);
    printNumber(7,1,0);
    printNumber(6,2,0);
    printNumber(5,3,0);
    oled.show()
    time.sleep(3)
    oled.fill(0)
    printNumber(0,0,0);
    printNumber(0,1,0);
    printNumber(0,2,0);
    printNumber(9,3,0);
    oled.show()
    time.sleep(3)