# WH 2nd string method notes

name = input("what is name: ").title().strip()
name_space = 0
age = float(input("give your age: "))
# .lower() all lower case
# .upper() all upper case
# .capitalize() capitalizes the first letter
# .title() capitalizes all of the first letters
for space_name in name:
    if space_name in " ":
      name_space += 1
if name_space < 3:
     print(f"hello {name}, it is nice to meat you! I can't believe you are {age: .0f}.")
else:
    print("you are a bad person")

word = "brown"
sentence = "the quick brown fox jumps over the lazy dog"
start = sentence.find(word)
length = len(word)
print(sentence.replace(word, "yellow"))