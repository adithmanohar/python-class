#forloop
#a=["apple","orange","watermelon","grapes"]
"""print(a[0])
print(a[1])
print(a[2])
print(a[3])"""
"""for i in range(0,3):
    print(a[i])"""
#.Write a program to calculate the sum of numbers from 1 to 100 using a for loop
"""sum=0
for i in range(0,101):
    
    sum=sum+i
print(sum)
"""
#write a program to print sum of even numbers from 0 to 100?using for loop
"""sum=0
for i in range(1,101):
    if i %2==0:
        sum+=i
print(sum)"""

#Nested loop
"""for i in range(0,5):
    for j in range(0,3):
          print("*",end=" ")
    print()
"""
#Print the following pattern using nested loops:
"""
*
* *
* * *
"""
"""for i in range(1,4):
    for j in range(i):
        print("*", end=" ")
    print()
"""
#2     outp  2
          # 2 4
          #2 4 6
"""for i in range(1,4):
    for j in range(1,1+i):
        print(2*j, end="   ")
    print()
    """
    #Print the following pattern using nested loops:
"""
   *
  * *
 * * *
    """
"""
row=int(input("enter row number"))
for i in range(1,row+1):
 # j loop is taken for SPACE printing
 for j in range(row-i):
    print(" ",end="")
 for k in range(i):
        print("*", end=" ")
 print()
 """
#Print the following pattern using nested loops:
"""
    1
   1 2
  1 2 3
 1 2 3 4
 """
"""
rows = 4
for i in range(1, rows + 1):

    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print numbers from 1 to i
    for k in range(1, i + 1):
        print(k, end=" ")

    print() # Move to the next line
"""
#whileloop
"""
x=int(input("enter number"))
while x!=0:
    x=int(input("enter number"))
print("you entered zero so you exited from the loop")
"""
"""
x=0
while x<=10:
    print(x)
    x=x+1
    """
"""x=0
sum=0
while x<=10:
    sum=sum+x
    x=x+1
print(sum)
"""
#multiplication of 3
"""x=1
while x<=10:
   print( f" {x}*3={x*3}")
   x=x+1
         """
#multiplication of 4 upto 20
"""
x=1
mul=1
while mul<=20:
    mul=4*x
   
    print(mul)
    x=x+1
    """
#write a program to print the multiples of 4 between 20 and 30
'''
x=6
mul=20
while mul>=20 and mul<= 30:

   
    print(mul)
    
    mul=4*x
    x=x+1
'''
#write a program to find the largest  number among 3 number--user give input
"""
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b:
    if a>c:
        print(f"{a} is largest")
elif b>a and b>c:
       print(f"{b} is largest")
else:       
  print (f"{c} is largest")   
  """
