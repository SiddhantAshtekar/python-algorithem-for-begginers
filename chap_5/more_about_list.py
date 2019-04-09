num=list(range(1,11))
print(num)
popped_value=num.pop()
print(popped_value)
n1=[1,3,4,5,6,7,8,9,1,3,3,51]
# print(n1.index(1,9))

def negative_list(l):
    negatinve=[]
    for i in l:
        negatinve.append(-i)
    return negatinve
print(negative_list(n1))