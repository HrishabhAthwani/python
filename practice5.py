numb1 = 18
numb2 = int(input("Guess a number : "))
if numb1 == numb2:
    print("Congratulations !! ,you win")
elif numb1 > numb2:
    print("Too low")
elif numb1 < numb2:
    print("Too high")
else:
    print("Enter a valid")