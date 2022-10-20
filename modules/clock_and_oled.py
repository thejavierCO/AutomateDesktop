import urequests
import utime
from machine import RTC
from env import page_realtime

rtc = RTC()

def clock(arg, intervalo_peticiones=60, ultima_peticion=0):
    try:
        while True:
            if (utime.time() - ultima_peticion) >= intervalo_peticiones:
                try:
                    response = urequests.get(page_realtime)
                    if response.status_code == 200:
                        data = response.json()
                        rtc.datetime((data["year"], data["month"], data["day"], 0, data["hour"],
                                     data["minute"], data["seconds"], data["milliSeconds"]))
                        ultima_peticion = utime.time()
                except Exception as err:
                    print(err)
            oled.fill(0)
            date_numbers = []
            for i in range(3):
                n = int("{4:02d}:{5:02d}:{6:02d}".format(
                    *rtc.datetime()).split(":")[i])
                n0 = int(n/10)
                n1 = int(n-int(n0*10))
                date_numbers.append(n0)
                date_numbers.append(n1)
            oled.graphic(numbers.Render(date_numbers[0], 24, 32), 4*24, 0)
            oled.graphic(numbers.Render(date_numbers[1], 24, 32), 3*24, 0)
            oled.graphic(numbers.Render(date_numbers[2], 24, 32), 2*24, 0)
            oled.graphic(numbers.Render(date_numbers[3], 24, 32), 1*24, 0)
            oled.show()
            utime.sleep(0.1)
    except NameError as err:
        print(err)
        oled.fill(0)
        oled.invert(True)
        oled.text("Error",0,0)
        oled.show()
        utime.sleep(3)
