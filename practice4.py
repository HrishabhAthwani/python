numb1 = 18
def guess():
    numb2 = int(input("Guess a number : "))
    if numb1 == numb2:
        print("Congratulations !! ,you win")
    elif numb1 > numb2:
        print("Too low")
        guess()
    elif numb1 < numb2:
        print("Too high")
        guess()
    else:
        print("Enter a valid number")
        guess()

guess()
