def num(i):
    sum=0
    

    if i==0:
        return 0



    return (i % 10)+ num(i // 10)

print(num(12345))