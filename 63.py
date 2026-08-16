arr = [3, 7, 2, 9, 5, 1]

small=arr[0]
sec_small=arr[0]

for i in arr:
    if i<small:
        sec_small=small
        small=i
    elif i<sec_small and i!=small:
        sec_small=i
print(sec_small)