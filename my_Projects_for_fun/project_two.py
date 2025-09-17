# WH 2nd not for class

file_name = "C:/Users/tyler.hurst/Desktop/"
while_number = 1
while_print = int(input("how many: "))+1
if while_print < 501:
    while while_number != while_print :
        with open(file_name+f"Document{while_number}.txt", 'w') as file:
            content = file.write("hi")
        while_number += 1