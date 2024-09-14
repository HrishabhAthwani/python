alphs = ["abc", "def", "ghi"]

def rev(l):
    elem = []
    for i in l:
        elem.append(i[::-1])
    return elem

print(rev(alphs))