import random
win_numb = random.randint(1,100)
guess_numb = int(input("Guess the number (Between 1-100) : "))
counter = 1
while win_numb != guess_numb:
    if win_numb > guess_numb:
        print("Too low")
        guess_numb = int(input("Guess the number (Between 1-100) : "))
        counter += 1
        continue
    elif win_numb < guess_numb:
        print("Too high")
        guess_numb = int(input("Guess the number (Between 1-100) : "))
        counter += 1 
        continue
print(f"You win !!,you took {counter} guess") 
