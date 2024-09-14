name = input("Enter your name : ")
length = len(name)
i = 0
x = ""
while i<length:
    if name[i] not in x:
        x += name[i]
    print(f"{name[ i]} : {name.count(name[i])}")
    i+=1