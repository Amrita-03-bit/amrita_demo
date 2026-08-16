arr = [3, 4, -1, 1]
n=len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

excepted=1
for i in range(n):
    if arr[i]== excepted:
        excepted+=1

print(excepted)

