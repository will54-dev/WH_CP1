# WH 2nd average grade progect

english = float(input("what is your grade in english: "))
progaming = float(input("what is your grade in progaming: "))
biology = float(input("what is your grade in biology: "))
avisory = float(input("what is your grade in avisory: "))
math = float(input("what is your grade in math: "))
art = float(input("what is your grade in art: "))
history = float(input("what is your grade in history: "))

print("your average grade is", round((english+progaming+biology+avisory+math+art+history)/7*100)/100)