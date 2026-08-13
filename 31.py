def max(n,i,lar):

    if i==len(n):
        return lar
    if n[i]>lar:
        lar=n[i]


    return max(n,i+1,lar)

print(max([10,20,30,40,50],0,0))