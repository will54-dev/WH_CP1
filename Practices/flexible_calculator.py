# Wh 2nd flexible caculator

#function for mutiple equal stetmnts
def multequl(var,*check):
    #set out to false
    out = False
    #loop for check in check
    for check in check:
        #if var is = to check
        if var == check:
            #set out to true
            out = True
    #output out
    return out

# define a function for avreg
def avrag(*imput):
    #set sum to 0
    sum = 0
    #set count to 0
    count = 0
    #loop for item in imput
    for item in imput:
        #if it is an number and it to sum
        if isinstance(item, (float,int)): 
            sum += item
            #add 1 to count
            count += 1
        #if item is a lsit 
        elif isinstance(item, (list)):
            #loop for l in item
            for l in item:
                #if it is an number and it to sum
                if isinstance(l, (float,int)): 
                    sum += l
                    #add 1 to count
                    count += 1
    #if count is empty retun zero error
    if count == 0: return "Zero Error"
    #output sum devided by count
    return sum/count

# define a function for producut
def product(*imput):
    #set pr to 1
    pr = 1
    #loop for item in imput
    for item in imput:
        #mutiply pr to item if it is a number
        if isinstance(item, (float,int)): pr *= item
        #if item is a list
        elif isinstance(item, (list)):
            #loop of l in item
            for l in item:
                #mutiply pr to item if it is a number
                if isinstance(l, (float,int)): pr *= l
    #output pr
    return pr

#define a function for the main user interaction
def userInputs():
        #set numbers as a list
        numbers = []
        #show that they can imput numbers and done to finish
        print("Type a number and enter or type done when done.")
        #loop
        while True:
            #set num to input
            num = input().strip().lower()
            #if number is an interger and has only one .
            try:
                num = float(num)
                #add num to number
                numbers.append(num)
            except:
                #if num is done
                if multequl(num ,"done", ""):
                    #if numbers is empty output 0
                    if numbers  == []: return [0]
                    #output numbers
                    return numbers
                #else
                else:
                    #show not a number
                    print("Not a number.")

# main loop
while True:
    #pmt the user to pick an oporation
    want = input("\npick one.\n1. Sum\n2. Average\n3. Max\n4. Min\n5. Product\n6. exit\n").lower().strip()

    #if the user pickes sum
    if multequl(want, "1", "sum"):
        print(sum(userInputs()))

    #if the user pickes sum
    elif multequl(want, "2", "average"):
        print(avrag(userInputs()))

    #if the user pickes sum
    elif multequl(want, "3", "max"):
        print(max(userInputs()))

    #if the user pickes sum
    elif multequl(want, "4", "min"):
        print(min(userInputs()))

    #if the user pickes sum
    elif multequl(want, "5", "product"):
        print(product(userInputs()))

    #if user wants to exit 
    elif multequl(want, "6", "exit"):
        #exit
        break

    else:
        print("Not an option.")
