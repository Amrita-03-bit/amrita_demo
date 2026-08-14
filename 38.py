arr = [10, 20, 30, 40, 50]

index=2

for i in range(index,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()
print(arr)    
