def e(l):
    e=[]
    for i in l:
            if i%2==0:
                e.append(i)
    return e
def o(l):
    o=[]
    for i in l:
            if i%2==1:
                o.append(i)
    return o
def oe(l):
    n=[]
    n.append(o(l))
    n.append(e(l))
    return n
n1=list(range(1,11))
print(oe(n1))
