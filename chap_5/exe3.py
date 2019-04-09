def r(l):
    n=[]
    for i in l:
        pop=i
        n.append(pop[::-1])
    return n
n1=['sid','aish','uma']
print(r(n1))