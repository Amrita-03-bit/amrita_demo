arr = [1, 2, 3, 5, 6]
n=6
actual_sum=0
excepted_sum=n*(n+1)//2
for i in arr:
     actual_sum+=i

missing_num=excepted_sum - actual_sum

print(missing_num)