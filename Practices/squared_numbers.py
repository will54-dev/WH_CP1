#Wh 2nd square numbers, list to run the program
'[print(f"{i**.5}^2={i}")for(i)in map(lambda n:n**2,range(99))]'
[print(f"{i**.5}^2={i}")for(i)in map(lambda n:n**2,[x*0+list(map(lambda i:float(i)if i.isnumeric()else 0,input(f"number {x+1}:")))[0]for x in range(20)])]