# WH 2nd while loop notes.
import time
import random

#Infinite loop
num = 0
break_point = random.randint(1,50)
while num <+ 20:
    time.sleep(0.15)
    num += 1 #fix it
    if num == break_point:
        break
    elif num == 5:
        continue
    print(num)
else:
    print("good")