arr = [10, 5, 25, 8, 40, 15]

lar=arr[0]
sec_lar=arr[0]
for i in arr:
    if i>lar:
        sec_lar=lar
        lar=i
    else:
      if i>sec_lar and i!=lar:
         sec_lar=i

print(sec_lar)