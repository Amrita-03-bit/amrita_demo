def sum(n,i):

    if i==len(n):
        return 0

        

    return n[i]+sum(n,i+1)

print(sum([2,4,6,8,10],0))