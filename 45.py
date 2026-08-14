arr = [1, 2, 2, 3, 4, 3, 5, 2]

new_arr=[]

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)        
