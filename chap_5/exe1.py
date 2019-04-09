num=list(range(1,11,2))
def sq(l):
    n=[]
    for i in l:
        n.append(i**2)
    return n
print(sq(num))