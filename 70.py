try:
    a=int(input("enter a number :"))
    b=int(input("enter a number :"))

    print(a/b)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("invalid input")    
