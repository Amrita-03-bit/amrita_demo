def calculate_average(*nums):

    average=0
    total_number=0

    for i in nums:
        total_number+=i

    average=total_number/len(nums)  

    return average

print(calculate_average(34,654,795,235))  

    