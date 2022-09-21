
""" 
3. Write a python script to handle the ArithmeticError
 """
print("Enter the two numbers:") 
x,y=int(input()) ,int(input())
try:
    c=x/y

except ArithmeticError:
    print("Please check your input values.")
except Exception:
    print("Some thing wrong!!!")   

#====================================output===================================
""" 
Enter the two numbers:
67
0
Please check your input values.
 """     
