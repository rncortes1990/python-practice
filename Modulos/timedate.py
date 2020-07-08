import datetime
import pytz
dt =datetime.datetime.now(pytz.timezone('America/Santiago'))
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.tzinfo)
print(dt.isoformat())
import locale
import os
os.environ['TZ'] = 'America/Santiago'
os.system("tzutil /s \"Central Standard Time\"");
locale.setlocale(locale.LC_ALL,'')
print(dt.strftime("%A %d %B %Y %H:%M"))
t = datetime.timedelta(days=10,hours=3,seconds=400)
print (dt)
en2semanas = dt + t
print(en2semanas)
hace2semanas = dt - t
print(hace2semanas)