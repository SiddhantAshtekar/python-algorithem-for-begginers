user_name=input("Input your name:")
i=0
var =""
while i<len(user_name):
    if user_name[i] not in var:
        var +=user_name[i]
        print(f"{user_name[i]}:{user_name.count(user_name[i])}")
    i=i+1