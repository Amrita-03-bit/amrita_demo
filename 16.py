def find_duplicates(nums):

    freq={}
    duplicates=[]

    for i in nums:
        if i in freq:
            freq[i]+=1

        else:
            freq[i]=1

    for j in freq:
        if freq[j]>1:
         duplicates.append(j)

    return duplicates  

    #return None      


nums = [1, 2, 3, 2, 4, 5, 1, 6]
print(find_duplicates(nums))          
