arr = [2, 4, 6, 8, 10, 12]

lar=arr[0]
small=arr[0]

for i in arr:
    if i>lar:
        lar=i

    if i<small:
        small=i

print(lar - small)            