arr = [2, 4, 1, 3, 5]

total=0
prefix_num=[]

for i in arr:
    total+=i
    prefix_num.append(total)
print(prefix_num)
