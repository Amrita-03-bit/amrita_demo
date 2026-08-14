arr = [10, 20, 30, 40, 50,0]

index=2
value=25
for i in range(len(arr)-1,2,-1):
    arr[i]=arr[i-1]
arr[2]=25
for i in range(len(arr)):
    print(arr[i])
