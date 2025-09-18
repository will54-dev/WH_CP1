# WH 2nd booleans notes

import time
import datetime as date

over = False
print(over)
name = ""
print(bool(name))

curent_time = time.time()
read_time = time.ctime(curent_time)
print(f"time: {read_time}")

now = date.datetime.now()
hour = now.strftime("%H")

# month = %m  (%b, %b)
# day = %d
# year = %Y or %y
# hour = %H
# minutes = %M
# seconds = %S

print(f"the time is now {now}")
print(f'hour is:{hour}')
print(f"my hour variable is a string: {isinstance(hour, str)}")
print(f"my hour variable is a interger: {isinstance(hour, int)}")
print(f"my hour variable is a float: {isinstance(hour, float)}")