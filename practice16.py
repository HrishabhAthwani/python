numbers = [1,2,3,4,5,11],[1,5,7,11,12,20]
def common(l1,l2):
    common_numbs = []
    for i in l1:
        if i in l2:
            common_numbs.append(i)
    return(common_numbs)

print(common([1,2,3,4,5,11],[1,5,7.11,12,20]))
