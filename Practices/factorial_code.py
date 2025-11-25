#WH 2nd factorial

#while imput isnt numaric request input
r = [1]; imput = [x*list(map(lambda i:int(i) if i.isnumeric() else [0,r.append(1)][0], [input()]))[0] for x in r][-1]

#def calc(num
def calc(num):
    #number = 1
    number = 1
    #fro i in range(n+1) number r*= i
    #fix make range add after 
    for i in range(num): i += 1; number*= i
    #return number
    return number

#print("original num{input}, output {calc(num)}")
print(f"orignal num {imput}, output {calc(imput)}")