x = 5 #global var
def func1():
    y = 7 #local var1
    return y

def func2():
    print(y) #y out of its scope coz y is not its local var

print(x)
print(func1())
print(func2())
