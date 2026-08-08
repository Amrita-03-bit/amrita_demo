Input= [1, 2, 2, 3, 1, 2, 4]

count=0
freq={}

for i in Input:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1

for key,values in freq.items():
     if freq[key]>1:
         count+=1
         #print(key,"=" ,values)
     else:
          freq[key]==1
            # print(key,"=" ,values)   
print(freq)            
            