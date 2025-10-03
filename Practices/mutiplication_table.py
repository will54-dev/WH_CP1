# WH 2nd multiplication table practice

numbers = range(1,13)
lists = "1   "
print("x   1   2   3   4   5   6   7   8   9   10  11  12")
for x in numbers:
    for c in numbers:
        if x*c < 10:
            lists = f"{lists}{(x*c)}   "
        elif x*c < 100:
            lists = f"{lists}{(x*c)}  "
        else:
            lists = f"{lists}{(x*c)} "
    {print(lists)}
    if x+1 < 10: lists = f"{x+1}   "
    else: lists = f"{x+1}  "