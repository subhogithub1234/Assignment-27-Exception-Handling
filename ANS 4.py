""" 
4. Write a python script to handle a ValueError

 """


try:
    x=int(input("Enter the 1st number:"))
    y=int(input("Enter the second number:"))
    z=x/y
    print("Result is:",z)  
   
except ValueError:
    print("Plz enter the right values.")
except Exception:
    print("Some things is wrong in your program.")    

#====================================OUTPUT========================================
""" 
Enter the 1st number:67
Enter the second number:ff
Plz enter the right values.
 """    
      
