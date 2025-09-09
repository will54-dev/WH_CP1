# WH 2nd calculator practice

while_ch = 0


def number_che(number):
    number_len = 0
    for number_digit in number:
        if number_digit in "1234567890.":
            number_len +=1
    if number_len == len(number):
        return True
        
while while_ch == 0:
    number_1 = input("give a number: ")
    if number_che(number_1):
        while_ch = 1
