arr = [2, 4, 6, 2, 8, 4, 10, 6]

freq={}

for i in arr:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1

for j in freq:
    if freq[j]>1:
        print(j)  
                