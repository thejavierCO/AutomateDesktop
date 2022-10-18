from machine import Pin, PWM
import framebuf
import time

class Btn:
    def __init__(self,pin,nc=False):
        self.pin = Pin(pin,Pin.IN)
        self.lastclick = 0
        self.nc = nc
    def updateTime(self):
        if self.Read() == False:
            self.lastclick = 0
    def Read(self):
        if self.nc == False:
            return self.pin.value()
        else:
            return not self.pin.value()
    def timeclick(self):
        if self.Read() == True:
            if self.lastclick == 0:
                self.lastclick = time.time()
        return time.time() - self.lastclick

class Led:
    def __init__ (self, pin, pwm = False):
        self.pin = Pin(pin,Pin.OUT)
        self.pwm = pwm
        if pwm:
            self.pwm = PWM(Pin(pin))
        self.duty = 0
        self.once = False
        
    def Read(self):
        if self.pwm == False:
            return Bool(self.pin.value())
        else:
            return self.duty
        
    def Write(self,value):
        if self.pwm == False:
            if value == True:
                self.On()
            else:
                self.Off()
        else:
            self.set_intencidad(value)
        
    def On(self):
        if self.pwm:
            print("using pwm")
        else:
            self.pin.on()
    def Off(self):
        if self.pwm:
            print("using pwm")
        else:
            self.pin.off()

    def set_intencidad(self,duty,freq=60):
        if not self.pwm:
            print("not using pwm")
        else:
            if duty >= 1023:
                duty = 1023
            elif duty <= 0:
                duty = 0
            self.pwm.freq(freq)
            self.pwm.duty(duty)
            self.duty = duty
            
    def once_reset(self):
        if self.pwm == False:
            print("not using pwm")
        else:
            self.once = False
    def once_intencidad(self,duty,freq=60):
        if self.pwm == False:
            print("not using pwm")
        else:
            if self.once == False:
                self.set_intencidad(duty,freq)
                self.once = True
class iconsbuffer:
    def __init__(self):
        self.listicons = []
    
    def add(self,file):
        buffer = bytearray()
        with open(file,"rb") as f:
            f.readline()
            f.readline()
            buffer = bytearray(f.read())
        f.close()
        self.listicons.append(buffer)
        return self
    def get(self,index):
        return self.listicons[int(index)]
    
class Numbersbuffer:
    def __init__(self,listNumbers):
        self.basic = iconsbuffer()
        for icon in listNumbers:
            self.basic.add(icon)
    def get(self,number):
        datalist = []
        if number <= 9:
            datalist.append(self.Render(self.basic.get(number)))
        else:
            for n in range(len(str(number))):
                datalist.append(self.Render(self.basic.get(str(number)[n])))
        return datalist
    def Render(self,number,w,h):
        return framebuf.FrameBuffer(number,w,h,framebuf.MONO_HLSB)
        