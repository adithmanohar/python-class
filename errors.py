#exception
"""
try:
 x=10/0
 print(x)
except  ZeroDivisionError:
 print("you cant divide by zero")

print(2+3)
"""

"""
a=int(input("enter your number"))
try:  
 print(10/a)

except  ZeroDivisionError:
 print("you cant divide by zero")
else:
 print(f"result is{10/a}")
finally: 
 print("this will be always printed")
"""
#raising exception

x=int(input("enter the number"))
if x<0 :
 raise ValueError("negative number are a error")
else :
 print(x+2)