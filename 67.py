arr = [1, -2, 3, -4, 5, -6, 7]

positive=0

for negative in range(len(arr)):
    if  arr[negative]<0:
        arr[positive],arr[negative]=arr[negative],arr[positive]
        positive+=1


print(arr)        
