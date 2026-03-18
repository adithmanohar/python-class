"""a=7
b=10
print(a+b)
c=5
d=15
print(c+d)
e=10
f=20
"""
# using function

#method 1
"""
def add (a,b):#parameters
    print(a+b)
add(7,10)    
add(5,15)
add(10,20)#arguments
"""
#method 2
"""
def substract (a,b):
    return a-b
print( substract(10,5))
"""
#method 3
"""
def multiply (a,b):
    return a*b
mul=multiply (10,10)
print(mul)
"""
#method 3.1
"""
def multiply (a,b):
    print( a*b)
multiply (10,10)
"""
#type of arguments

#postional arguments
"""
def substract (a,b):
    return a-b
print( substract(10,5))
"""
#keyword of arguments
"""
def printdetails (**kwargs):
    for keyy,valuee in kwargs.items():
        print(f"{keyy}{valuee}")
printdetails(name="adith",age=22,city="kottakkal")
"""
#arbitrary arguments
"""
def sumnumbers (*args):
    total=0
    for number in args :
        total=total+number
    print(total)
sumnumbers(1,2,3,4,5)
"""
"""
def substractumber (b,*args):
    for number in args:
     print(b-number)
substractumber(10,5,15,7)
"""

#TASK

# Write a function reverse_string(text) that reverses a string without using slicing ([::-1]).
#Use a for loop to build the reversed string.
"""
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text=char+reversed_text
    return reversed_text
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
#Write a function show_employee(name, **kwargs) that prints the employee name andany other details passed using keyword arguments.
'''
def show_employee(name, **kwargs):
    print(f"Employee Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
'''
#lambda functions
'''
def add (a,b):
    c=a+b
    print(c)
add(10,10)
'''
'''
addd=lambda a,b,c:a+b+c #syntax
print(addd(10,20,30))
'''
#higherorder function
'''
def increment (n):
    return lambda x:x+n
a=increment(10)
print(a(10))
'''
'''
def substract(a,b):
    return a-b
a=substract(10,5)
print(a)
'''
#lambda function with higher order function

#1-MAP
'''
numbers=[1,2,3,4]
abc= map(lambda x:x**2,numbers)
print(list(abc))
#2
numbers=[1,2,3,4,5,6,7,8,9,10]
abc= map(lambda x:x*2,numbers)
print(list(abc))
'''

# 2-filter
'''
a=[1,2,3,4,5,6,7,8,9,10]
abc=filter(lambda x:x%2==0,a)
print(list(abc))
'''
# 3-reduce
'''
from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
abc=reduce(lambda x,y:x+y,a)
print(abc)
'''

#recursion(fuction e veendum veendum call cheya)The problem can be divided into smaller subproblems of the same type


#define a function named factorial with parameter n
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n* factorial(n-1)
print(factorial(5))
"""
#fibonacci 
"""
def fibonacci(n):
  if n<=1:
    return n
  else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))
"""
# print series fibboanic
"""
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
a=int(input("enter a number"))
for i in range(a):
 print(fibonacci(i),end=" ")

 """

#write a program to print the sum of the numbers in the list using recursion
"""
def sum (n):
    if not n:
        return 0
    return n[0]+sum(n[1:])
print( sum([1,2,3,4,5]))
"""

#tail Recursion
"""
def tailfactorial (n,accumulator=1):
    if n==0 or n==1:
        return accumulator
    else:
        return tailfactorial(n-1,accumulator*n)
print(tailfactorial(5))
"""
#functionscope

x=10 #(global scope)
def outerfunction():
    x=5#(enclosing scope)
    print(x)
    
    def innerfunction():
        x=2 #(local scope)
        print(x)
    innerfunction() 

outerfunction()
print(x)       
