def most_frequent(nums):

    freq={}

    for i in nums:
        if i in freq:
            freq[i]+=1

        else:
            freq[i]=1

    high_freq=0
    result=None
    for j in freq:
        if freq[j]>high_freq:
         
         high_freq=freq[j]
         result=j

    return   result

      

nums = [1, 2, 2, 3, 1, 2, 4]
print(most_frequent(nums))   


