#Write a program to find the largest of three numbers without using the max() function. 

"""
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b and a>c:
    print("Largest number is:",a)
elif b>c:
    print("Largest number is:",b)
else:
    print("Largest number is:",c)
"""

#Given a string, count how  many vowels are present in it
"""
text=input("Enter a string:")
count=0
for char in text:
    if char in "aeiou":
        count+=1
print("Number of vowels:",count)

"""
#Write a Python program to remove duplicates from a list while keeping the order.
"""
abc=[1,2,3,2,3,5,4,1,5]
bcd=[]
for item in abc:
    if item not in bcd:
        bcd.append(item)
print("List without duplicates:",bcd)
"""
 #Take a list of integers and print the sum of all even numbers.
""" 
number=[1,2,3,4,5,6,7,8,9,10]
sumeven=0
for i in number:
    if i%2==0:
        sumeven+=i
print(f"um of even numbers:{sumeven}")
"""
#Given a sentence, print the number of words in it. 
"""
sentence = "i am adith manohar."
words=sentence.split()
count=len(words)
print("Number of words:",count)
"""

#Write a program to check whether a number is prime or not.

num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")










# Reverse a string without using any built-in reverse functions

string = input("Enter a string: ")
reversstring = ""
for char in string:
    reversstring=char+reversstring  
print("Reversed string is-:",reversstring)



#Write a program to count how many times each character appears in a string.

A=input("Enter a string:")

count={}

for i in A:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)


#Write a program to merge two sorted lists into one sorted list without using sort()





#Write a function that takes a list of numbers and returns a new list containing only the unique elements. 

def unique_list(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
print(unique_list([1,1,2,2,3,5,4,3,5]))

#Write a program to check if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
s1="listen"
s2="silent"
if are_anagrams(s1,s2):
    print("Anagrams")
else:
    print("Not Anagrams")




#  Write a function to find the second largest number in a list.

def second_largest(nums):
    first=second=float('-inf')
    for num in nums:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num        
    return second
numbers=[10,20,4,45,99]
print("Second largest:",second_largest(numbers))


#Write a lambda expressionwith filter() to extract only odd numbers from a list.

numbers=[1,2,3,4,5,6,7,8,9]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)

#impliment a simple calculator using function substract,add

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Addition:",add(a,b))
print("Subtraction:",subtract(a,b))


#Write a function that returns Fibonacci numbers using recusion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a number:"))
print("Fibonacci number:",fibonacci(n))

#Create a class Student with attributes name, age, and marks. Add a method to display the student's details.
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Marks:{self.marks}")
student1=Student("Adith",22,95)
student1.display_details()

#Create a class BankAccount with methods deposit(), withdraw(),and check_balance().Prevent withdrawing more than the balance.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited:{amount}.New balance:{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance!")
        else:
            self.balance-=amount
            print(f"Withdrawn:{amount}.New balance:{self.balance}")
    def check_balance(self):
        print(f"Balance for {self.owner}:{self.balance}")
account = BankAccount("Adith", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500) 
account.check_balance()

#Implement a class Car with private attributes for mode l and price. Provide getter and setter methods.


class Car:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def getmodel(self):
        return self.model
    def setmodel(self,model):
        self.model=model

    def getprice(self):
        return self.price
    def set_price(self,price):
        self.price=price
        
mycar=Car("Toyota",20000)
print("Model:",mycar.getmodel())
print("Price:",mycar.getprice())
mycar.set_model("Honda")
mycar.set_price(22000)
print("Updated Model:",mycar.getmodel())
print("Updated Price:",mycar.getprice())

#Write a program using inheritance: create a base class Animal andsubclasses Dog and Cat. Each should have its own sound () method.

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass 
class Dog(Animal):
    def sound(self):
        print(f"{self.name}says:Woof Woof!")
class Cat(Animal):
    def sound(self):
        print(f"{self.name}says:Meow!")
dog1 = Dog("Bady")
cat1 = Cat("Katty")
dog1.sound()
cat1.sound()

#Use method overriding to show how the same method behaves differently in parent and child classes.

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a button.")


v=Vehicle()
c=Car()
b=Bike()
v.start()
c.start()
b.start() 

#Demonstrate operator overloading by creating a class Distance that overloads the + operator to add two distance objects.

class Distance:
    def __init__(self,meters):
        self.meters=meters
    def __add__(self,other):
        return Distance(self.meters+other.meter)
    def display(self):
        print(f"Distance:{self.meters} meters")
d1=Distance(100)
d2=Distance(250)

d3=d1+d2
d3.display()


#Create a class Employee and a class Manager that inherits from Employee. Add extra attributes to Manager.


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
class Manager(Employee):
    def __init__(self, name,salary,department):
        super().__init__(name,salary)
        self.department=department   

    def display(self):
        super().display()
        print(f"Department:{self.department}")
emp1=Employee("adhi",50000)
mgr1=Manager("adith",80000,"HR")
print("Employee Details:")
emp1.display()
print("\nManager Details:")
mgr1.display()