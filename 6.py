


def second_largest_numb(nums):

    lar=float('-inf')
    second_lar_num=float('-inf')
    for i in nums:
        if i>lar:
            second_lar_num=lar
            lar=i
        

    
        elif  i>second_lar_num and i!= lar:
            second_lar_num=i
        

    return second_lar_num

nums = [10, 5, 8, 10, 3, 8]


print(second_largest_numb(nums))   