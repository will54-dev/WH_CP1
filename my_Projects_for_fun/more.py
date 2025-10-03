# WH 2nd for fun

number = 0
file_locate = f"C:/Users/william.haggard/Desktop/more_{number}.py"
copy_place =  "P:/Haggard, William/WH_CP1/my_Projects_for_fun/more.py"
with open(copy_place, 'r') as text:
    text = text.read()
    text = text.replace(str(number),str(number+1))
    print(text)
with open(file_locate, 'w') as x:
    x = x.write(text)