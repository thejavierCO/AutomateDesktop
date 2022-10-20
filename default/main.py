from clock import clock

oled.fill(0)

try:
    import _thread
    thread_available = True
except:
    thread_available = False

if thread_available:
    _thread.start_new_thread(clock, (60,))