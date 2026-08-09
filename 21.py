def find_missing_number(nums):

    total_nums=0
    lar=float('-inf')

    for j in nums:
        if j>lar:
            lar=j

    excepted_sum=0
    excepted_sum=lar*(lar+1)/2

    for i in nums:
        total_nums+=i

    missing_number=0
    missing_number=excepted_sum-total_nums
           

    



    return missing_number
nums = [1, 2, 3, 5, 6]
print(find_missing_number(nums))    