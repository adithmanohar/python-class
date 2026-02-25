# Write a function reverse_string(text) that reverses a string without using slicing ([::-1]).
#Use a for loop to build the reversed string.
"""
def reverse_string(text):
    reversed_text = "     "
    for  x in text:
     reversed_text=x+reversed_text
    return reversed_text      

a=input("Enter a string: ")
b= reverse_string(a)
print("Reversed string:",b)
"""
#Write a function is_prime(n) that returns True if a number is prime, and False otherwise.
"""
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n % i==0:
            return False
        
    else:
           return True  
number=int(input( "enter number"))

print(is_prime(number))
"""

#Write a function show_employee(name, **kwargs) that prints the employee name andany other details passed using keyword arguments. with output in python 
'''
def employee(name, **kwargs):
    print(f"Employee Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
employee("Alice", age=30, department="manager", salary=50000)
'''

#write a program to list prime numbers from 1 to 20
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n % i==0:
            return False
    else:
        return True
print("Prime numbers from 1 to 20 are:")
for a in range(1, 21):
 if is_prime(a):
  print(a)