arr = [2, 5, 8, 11, 14, 17]

even_num=0
odd_num=0

for i in arr:
    if i%2==0:
        even_num+=1

    else:
        odd_num+=1

print(f"total even number are : {even_num}\n total odd number are : {odd_num} ")            
