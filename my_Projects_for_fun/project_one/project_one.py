# WH 2nd not for class

names_txt = "C:/Users/william.haggard/Desktop/2nd haggard, william/WH_CP1/my_Projects_for_fun/project_one/numbers.txt"
name =  input("give your name: ")

with open(names_txt, "r") as name_list:
  the_name = name_list.read()
  for a_name in the_name:
    if a_name in name:
      print("yes")

with open(names_txt, "w") as name_write:
  name_write.write(name)
