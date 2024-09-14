def Fibbo(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b,  end=" ")
    else:
        print(a, b , end=" ")
        for i in range(n-2):
            c = a + b #c = 1, 2, 3, 5
            a = b     #a = 1, 1, 2, 3
            b = c     #b = 1, 2, 3, 5
            print(b , end =" ")

num = int(input("Enter how many no of terms of fibonacci series is required : "))
Fibbo(num)