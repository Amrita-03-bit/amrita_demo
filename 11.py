def majority_element(nums):

       freq={}

       for i in nums:
            if i in freq:
                  freq[i]+=1

            else:
                  freq[i]=1

       for j in freq:
             if freq[j]> len(nums)/2:

              return j

       return None    
                            
                     
nums = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums))