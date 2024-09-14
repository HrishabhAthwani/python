lists = [1,2,3,[1,2,3],4,5,6,[4,5,6]]

def l_counter(l):
    counter = 0
    for i in l:
        if type(i) == list:
            counter += 1
    return counter

print(l_counter(lists))
