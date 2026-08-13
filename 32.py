def even(n,i,count):
    if i==len(n):
        return count

    if n[i]%2==0:
        
        count+=1

    return even(n,i+1,count)

print(even([2,5,8,11,14,17],0,0))