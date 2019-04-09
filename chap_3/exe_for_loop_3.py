name=input("Enter your name:_")
var=""
for i in range(len(name)):
    if name[i] not in var:
        print(f"{name[i]}:{name.count(name[i])}")
        var+=name[i]