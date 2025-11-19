#Wh 2nd Mapping

numbers = [123,432,4,25325,435,4262,6432,53,25,435,435,435]
'''divide = []

for num in numbers:
    divided.append(num/2)'''


divide = list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} is {divide[i]}")