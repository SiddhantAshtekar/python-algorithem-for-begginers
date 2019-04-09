def rev(l):
    n=[]
    for i in range(len(l)):
        pop=l.pop()
        n.append(pop)
    return n
n1=list(range(1,5))
print(rev(n1))


n=list(range(1,5))
def reve(m):
    m.reverse()
    return m
print(reve(n))

n2=list(range(1,5))
def r(l):
    return l[::-1]
print(r(n2))