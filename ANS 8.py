""" 
8. Write a python script to implement try except and else block for division
 """
try:
    x=int(input("Enter the 1st number:"))
    y=int(input("Enter the 2nd number:"))
    
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Check your inputs.")
except ArithmeticError:
    print("Arithmetic issue.")
except Exception:
    print("Some things is wrong in your program.")
else:
       print("Result:",x/y)        

#================================OUTPUT=========================================
""" 
OUTPUT 1:
Enter the 1st number:56
Enter the 2nd number:bnn
Check your inputs.

OUTPUT 2:
Enter the 1st number:67
Enter the 2nd number:6  
Result: 11.166666666666666
 """