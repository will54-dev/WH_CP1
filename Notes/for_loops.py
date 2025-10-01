# WH 2nd for loops notes

numbers = [1,2,3,4,5,67,34,534,534,5,345,345,345,34,645,63,6,567,37,2,4,12,2436666666666666666666666666666666666666666666666666666666666666666666666666666]
import time
for number in numbers:
    number += 1
    if number > 40:
        number = str(number)
        print(number)
        for numbe in number:
            print(f"\t{numbe}")
    else:
        number += 10
        number = str(number)
        print(number)
        for numbe in number:
            print(f"\t{numbe}")



for x in range(1,11):
    time.sleep(1)
    print(x)
    for x in range(1,11):
        time.sleep(1)
        print(f"\t{x}")
        x = str(x)
        for x in x:
            print(f"\t\t{x}")