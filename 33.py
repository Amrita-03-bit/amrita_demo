def freq(n,i,target,count):

    if i==len(n):
        return count

    if n[i]==target:
        count+=1

    return freq(n,i+1,target,count)

print(freq([2,3,2,5,2,7],0,2,0))    