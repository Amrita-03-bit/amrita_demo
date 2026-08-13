def power(n,i):

    if i==0:
        return 1

    return n * power(n,i-1)

print(power(2,5))