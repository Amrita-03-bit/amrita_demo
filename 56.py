arr = [1, 2, 3, 4, 5, 6, 7]

first_max_num=arr[0]
sec_max_num=arr[0]
for i in arr:
    if i > first_max_num:
        sec_max_num=first_max_num
        first_max_num=i

    elif i>sec_max_num  and i!= first_max_num:
        sec_max_num=i

print(first_max_num + sec_max_num)


    