""" 
9. Write a python script to raise a ValueError.
 """
try:
    x=int(input("Enter the 1st number:"))
    y=int(input("Enter the 2nd number:"))
    if x==y:
        raise ArithmeticError()
    print(x/y)
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Check your inputs.")
except ArithmeticError:
    print("Arithmetic issue.")
except Exception:
    print("Some things is wrong in your program.") 

#================================OUTPUT=====================================
""" 
Enter the 1st number:5
Enter the 2nd number:5
Arithmetic issue.
 """         