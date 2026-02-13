'''a=int(input("enter a number"))
if a>100:
    print(f" {a} is greater than 100")
elif a>50 and a<100:
       print(f" {a} is between 50 and 100")

else:
       print(f" {a} is less than 50")'''


'''
num = int(input("Enter a number: "))

if num % 2 == 0:                                 # Check  number is even
    print("The number is Even")
    
    if num % 4 == 0:   
        
        print("It is also divisible by 4")
    else:
        print("It is not divisible by 4")

else:                                                  # Number is odd
    print("The number is Odd")
    
    if num % 3 == 0:  
        print("It is also divisible by 3")
    else:
        print("It is not divisible by 3")'''
#task 5
"""a = int(input("Enter marks "))
b = int(input("Enter attendance  "))

if a >=40:
     
     if b >=75:      
      print("pass") 
     else:
        print("fail")
else:
   print("fail")"""

   #task5
a=18 
print("Adult" if a>= 18 else "Minor")