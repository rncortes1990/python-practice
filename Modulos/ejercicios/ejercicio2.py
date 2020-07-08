import datetime
import time
import os
import pytz


def reloj():
    
    while True:
        dt =datetime.datetime.now(pytz.timezone('America/Santiago'))
        print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
        time.sleep(1)
        os.system('clear')

reloj()