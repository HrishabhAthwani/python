squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

squrs = [i**2 for i in range(1,11)]
print(squrs)


negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

neg = [-i for i in range(1,11)]
print(neg)


names = ["Hrishabh","Ayush","Shivam","Arshiya","Sumaiya","Akshat"]
l2 = []
for name in names:
    l2.append(name[0])
print(l2)

l3 = [name[0] for name in names]
print(l3)
