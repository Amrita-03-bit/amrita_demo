def rotate_num(nums,k):

    for i in range(k):
        last=nums[-1]

        for i in range(len(nums)-1,0,-1):
            nums[i]=nums[i-1]
        nums[0]=last  

    return nums      

nums = [1, 2, 3, 4, 5]
k = 2
print(rotate_num(nums,k))