""" 
7. Write a python script to add a finally block for the above script
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

finally:
    print("Program is end.")  

#=======================================OUTPUT=========================================
""" 
Enter the 1st number:5
Enter the 2nd number:0
Can't divide by zero.
Program is end.
 """