def calculator(a, b, operator):
    

    if operator=="+":
        return a+b

    elif operator =="-":
        return a-b

    elif operator =="*":
        return a*b

    elif operator =="/":
        return a/b

    else:
        return "invalid operator"

print(calculator(4,3,"+"))
print(calculator(6,5,"-"))   
print(calculator(3,2,"*"))
print(calculator(4,2,"/")) 