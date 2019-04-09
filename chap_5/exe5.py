def common(l1,l2):
    op=[]
    for i in l1:
        if i in l2:
            op.append(i)
    return op
n1=list(range(1,21,3))
n2=list(range(1,21,2))
print(common(n1,n2))

    