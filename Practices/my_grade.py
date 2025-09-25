# Wh 2nd what is my grade practice

grade = float(input("what is your grade as a present: "))

if grade >= 94:
    let_grade = "an A"
elif grade >= 90:
    let_grade = "an A-"
elif grade >= 87:
    let_grade = "a B"
elif grade >= 84:
    let_grade = "a B"
elif grade >= 80:
    let_grade = "a B-"
elif grade >= 77:
    let_grade = "a c+"
elif grade >= 75:
    let_grade = "a c"
elif grade >= 70:
    let_grade = "a c-"
elif grade >= 67:
    let_grade = "a D+"
elif grade >= 64:
    let_grade = "a D"
elif grade >= 60:
    let_grade = "a D-"
else:
    let_grade = "a F"

print(f"you have a {grade} that is {let_grade}")