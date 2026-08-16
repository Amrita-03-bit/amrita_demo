arr = [4, 7, 1, 9, 3, 2, 6]
target = 10

n=len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
#print(arr)         
target=10   

left=0
right=n-1

while left<=right:

    current_sum=arr[left]+arr[right]

    if current_sum==target:
        print(arr[left],arr[right])
        break
    if current_sum<target:
        left+=1

    else:
        right-=1    