numbers = [1,2,3,4,5,6,7,8,9,10]

def rev(l):
    reversed = []
    for i in range(len(l)):
        reversed.append(l.pop())
    return reversed

print(rev(numbers))