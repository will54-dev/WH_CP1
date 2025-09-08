# WH 2nd Idiot Proof

name = input("give your name: ")
phone = input("give your phone number: ")
gpa = input("give your GPA: ")
name_space = 0
name_replace = name

#name che
for space_name in name:
    if space_name in " ":
      name_space += 1
      name = name.replace("  "," ")
for space_name in name:
    if space_name in " ":
      name_space += 1
name_leter = len(name)-name_space
if name_leter//3 - name_space > 0:
   name = name.title().strip()
print(name_leter)
print(name_space)

