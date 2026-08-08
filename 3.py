Input= [10, 5, 20, 8, 20, 15]

largest=Input[0]
second_largest_number=Input[0]

for i in Input:
     if i>largest:
          largest=i

     else: 
         if i> second_largest_number and largest!=i  :
              second_largest_number=i

print(f"second largest number is : {second_largest_number}")              

