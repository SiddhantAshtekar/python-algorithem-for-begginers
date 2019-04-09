# 1 code example
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)
sq=[i**2 for i in range(1,11)]
print(sq)
# 2 code example
negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)
negative1=[-i for i in range(1,11)]
print(negative)
# 3 code example
name=['siddhant','milind','ashtekar']
re=[]
for i in name:
    re.append(i[0])
print(re)
rer=[i[0] for i in name]
print(rer)