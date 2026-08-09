def missing_number(nums):

    lar=float('-inf')

    for n in nums:
            if n>lar:
                lar=n 

    excepted_sum= lar*(lar+1)/2
    actual_sum=0
    for i in nums:
            actual_sum+=i
    

    missing_number=excepted_sum-actual_sum

    

     

    return  missing_number        

nums = [1, 2, 4, 5, 6]

print(missing_number(nums))