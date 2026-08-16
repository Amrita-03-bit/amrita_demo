arr = [1, 2, 3, 4, 5]

freq={}
for i in arr:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1
        
found=False
for j in freq:
    if freq[j]>1:
        found=True
        break

print(found)                     