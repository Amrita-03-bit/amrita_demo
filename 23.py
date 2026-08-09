def second_largest(nums):

    lar=float('-inf')
    sec_lar=float('-inf')

    for i in nums:
        if i>lar:
            sec_lar=lar
            lar=i
        elif i>sec_lar and i!=lar:
            sec_lar=i

    return sec_lar       

nums = [10, 5, 8, 10, 3, 8]
print(second_largest(nums))    