""" 
6. Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.
 """

try:
    print(
    """ 
    1.Addition.
    2.Substraction.
    3.Multiplaction.
    4.Division.
     """ )
    ch=int(input("Enter your choice:"))
    x=int(input("Enter 1st number:"))
    y=int(input("Enter the 2nd number:"))
    match ch:
        case 1:
            print("Result:",x+y) 
        case 2:
            print("Result:",x-y)
        case 3:        
            print("Result:",x*y)
        case 4:
            print("Result:",x//y)
except ZeroDivisionError:    
    print("Can't divide by zero.")
except ValueError:
    print("Check your inputs.")
except ArithmeticError:
    print("Arithmetic issue.")
except Exception:
    print("Some things is wrong in your program.")     

#===============================OUTPUT===============================================
""" 
Enter your choice:4
Enter 1st number:56
Enter the 2nd number:0
Can't divide by zero.
 """