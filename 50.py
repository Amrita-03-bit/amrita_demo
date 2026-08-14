arr = [2, 4, 1, 3, 5]
total=0
prefix=[]

for i in arr:
    total+=i
    prefix.append(total)

L=1
R=3

if L==0:
    result=prefix[R]

else:
    result=prefix[R]-prefix[L-1]

        
    
print(result)