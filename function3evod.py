def evod(numb):
    if numb%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


# OR

def check_evod(numb):
    print(numb%2 == 0)



a = int(input("Enter a number to checkif its even or odd : "))
evod(a)
check_evod(a)