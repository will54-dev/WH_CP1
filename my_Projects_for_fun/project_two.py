# WH 2nd not for class

file_name = "C:/Users/william.haggard/Desktop/"
while_number = 1
while_print = int(input("how many: "))+1
doc_tet = input("give the text")
if while_print < 501:
    while while_number != while_print :
        with open(file_name+f"Document{while_number}.txt", 'w') as file:
            content = file.write(doc_tet)
        while_number += 1