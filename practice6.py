name,age = input("Enter your name (space) your age : ").split()
age = int(age)
fstletter = name[0].upper()
if fstletter == "A" and age >= 10:
    print("you can watch movie coco")
else:
    print("Sorry you cant watch movie coco")