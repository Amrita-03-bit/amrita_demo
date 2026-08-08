nums = [1, 2, 2, 3, 1, 2, 4]

freq={}

for i in nums:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1


high=0
element= None
for j in freq:
      if freq[j]> high:
       high=freq[j]
       element=j

print(f" the  most repeting element is : {element} and  the frequence is : {high} ")                