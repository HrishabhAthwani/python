def greater(a,b):
    if a>b:
        print(f"{a} is bigger")
    elif b>a:
        print(f"{b} is bigger")
    else:
        print("Both are equal")

x,y = input("Enter two numbers : ").split()
x = int(x)
y = int(y)
greater(x,y)