def num(n,rev=0):
    
    
    
    if n==0:
        return rev

    digit=n%10
    rev=rev*10+digit
    return num(n// 10,rev)

print(num(12345))

    