def student(*marks, **details):

    average=0
    total_marks=0

    for i in marks:
        total_marks+=i

    average=total_marks/len(marks)


    details["average"]=average

    print("details",details)
    

student( 39,3,4,56,7,name="riya",couse="MCA")  


