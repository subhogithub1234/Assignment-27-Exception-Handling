""" 
5. Write a python script to handle multiple Exception in one try
 """

try:
    x=int(input("Enter the 1st number:"))
    y=int(input("Enter the 2nd number:"))
    print("Result:",x/y)
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Check your inputs.")
except ArithmeticError:
    print("Arithmetic issue.")
except Exception:
    print("Some things is wrong in your program.")     

#================================OUTPUT========================================
""" 
     Enter the 1st number:78
Enter the 2nd number:hhjg
Check your inputs.
"""           