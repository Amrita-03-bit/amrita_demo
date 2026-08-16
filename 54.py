arr = [1, 2, 3, 4, 5, 6, 7, 8]

left=0
right=len(arr)-1
ans=10

while left<=right:

    current_sum=arr[left]+arr[right]

    if current_sum==ans:
        print(arr[left],arr[right])
        break
    if current_sum<ans:
        left+=1

    else:
        right-=1

         
