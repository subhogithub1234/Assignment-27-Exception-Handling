""" 
10. Write a python script to implemented a nested Try Except block.
 """
print("Enter the two numbers:") 

try:
    x,y=int(input()) ,int(input())
   
    try:
         c=x/y
         print(c) 
    except ArithmeticError:
            print("Please check your input values.")
            
except ValueError:
    print("Some thing wrong!!!")  

#===========================OUTPUT=======================================
""" 
OUTPUT 1:
Enter the two numbers:
56
hhhg
Some thing wrong!!!

OUTPUT 2:
Enter the two numbers:
56
0
Please check your input values.
 """     