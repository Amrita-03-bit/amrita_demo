arr = [2, 4, 6, 8, 10]

difference=arr[1]-arr[0]
found=True
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]!=difference:
        found=False
        break
print(found)    