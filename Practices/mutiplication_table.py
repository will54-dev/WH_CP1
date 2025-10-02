# WH 2nd multiplication table practice

numbers = range(1,13);lists = "1   ";print("x   1   2   3   4   5   6   7   8   9   10  11  12")
for x in numbers:
    for c in numbers:
        lists = f"{lists}{(x*c)}   "if x*c < 10 else lists; lists = f"{lists}{(x*c)}  " if x*c < 100 else lists; lists = f"{lists}{(x*c)} " if x*c < 1000 else lists
    print(lists)
    lists = f"{x+1}   " if x+1 < 10 else f"{x+1}  "