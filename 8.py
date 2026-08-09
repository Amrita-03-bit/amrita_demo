def nums(num):
    slow=0


    for fast in range(len(num)):
        if num[fast]!=0:
            num[slow],num[fast]=num[fast],num[slow]

            slow+=1
    return num

num = [0, 1, 0, 3, 12]



print(nums(num))