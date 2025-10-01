# WH 2nd multiplication table practice

numbers = range(1,13)
lists = "1"
print(numbers)
for x in numbers:
    for c in numbers:
        if x*c < 10:
            lists = f"{lists} {(x*c)}"
        elif x*c < 100:
            lists = f"{lists} {(x*c)}"

    print(lists)
    lists = str(x+1)