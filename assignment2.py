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












# Reverse a string without using any built-in reverse functions

string=input("Enter a string: ")
reversstring = ""
for char in string:
    reversed_string=char+reversstring  
print("Reversed string is -:",reversstring)