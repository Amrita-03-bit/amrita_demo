def student_result(name, marks, passing_marks=40):

    total_number=0
    percentage=0
    result=0

    for i in marks:
        total_number+=i

    percantage=total_number/(len(marks)*100)*100

    if total_number>=passing_marks:
        result="pass"

    else:
        result="fail"  

    return name,total_number,percantage,result     


marks = [75, 80, 65, 90, 70]

print(student_result("Rahul", marks))
print(student_result("ankit",marks))