Input="aabbcdde"

freq={}

for i in Input:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1

for j in freq:
    if freq[j]==1:
        print(j)
        break
               

