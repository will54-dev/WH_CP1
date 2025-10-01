# WH 2nd multiplication table practice

numbers = range(1,13)
lists = []
listf = []
for x in numbers:
    for c in numbers:
        lists.append(x*c)
        print(lists)
    listf.extend(lists)
    lists = []
print(listf)