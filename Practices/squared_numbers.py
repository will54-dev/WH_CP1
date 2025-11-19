#Wh 2nd square numbers, list to run the program
'[print(f"{i**.5}^2={i}")for(i)in map(lambda n:n**2,range(99))]'
[print(f"{i**.5}^2={i}")for(i)in map(lambda n:n**2,[x*0+int(lambda x: x if isinstance(x,(int,float)) else 0,input())for(x)in range(20)])]