numbers = [1,2,3,4,5,6,7,8,9,10]
def sorter(l):
    even = []
    odd = []
    sorted_list = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    sorted_list = [even, odd]
    return sorted_list

print(sorter(numbers))