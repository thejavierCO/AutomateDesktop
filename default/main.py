from clock import clock

oled.fill(0)
oled.show()

try:
    import _thread
    thread_available = True
except:
    thread_available = False

if thread_available:
    oled.fill(0)
    oled.text("start clock",0,0)
    oled.show()
    try:
        _thread.start_new_thread(clock, (60,))
    except NameError  as err:
         oled.fill(0)
        oled.text(err,0,0)
        oled.show()
