#operators
'''a=1
b=3
print(a+b)#addition
a=4
b=2
print(a-b)#sub
a=6
b=3
print(a*b)#multi
a=10
b=5
print(a/b)#div
a=10
b=4
print(a%b)#mod
a=10
b=3
print(a//b)#floor division
a=2
b=4
print(a**b)#expontiation'''

#assigment operators
'''a=2
print(a)
a+=3      #a=a+3 add and assign
print(a)
a-=3      #a=a-3 sub and assign
print(a)
a/=2      #a=a/3 div and assign
print(a)
a*=3      #a=a*3 multi and assign
print(a)
a//=2     #a=a//2 #floor
print(a)
a**=2     #expo a=a**2
print(a)
a%=2      #a=a%2 mod
print(a)'''

#comparison operators
'''a=10
b=3
print(a==b)   #equalto
print(a!=b)   #NOT equalto
print(a>b)    #greaterthan
print(a<b)    #lessthan
a=3
print(a>=b)   #greaterthanorequalto
print(a<=b)   #lessthanorequalto '''

#Logical operators (both left and right are comparisons operators in any case pf logical operations)
'''#and
a=5
b=6
print(a==3 and b<10)     #andoprator    return TRUE if BOTH condition are  TRUE
print(a==3 or b<10)      #OR operators  return TRUE if one of the  condition is TRUE
print(not(a>3))          #not opertors        return TRUE if one condition is FALSE '''

 #membership operators
'''a=[1,2,3,4]
print(2 in a)             # to check the 2 in a (true) because a contains 2
print(2 not in a)        #to check 2 is not in a (false) because a contain 2
'''
#identity operators
'''a=2
b=2
print(a is b)

a=[1,2,3,4,5]
b=[1,2,3,4,5] 
print(a is b) #a and b points to diffrent memory locations in the case of list even though their values are same

a=(1,2,3,4)
b=(1,2,3,4) 
print(a is b)''' #same memory location

'''a={'name':'AdithManohar','age':'22'}    #dictionary
b={'name':'AdithManohar','age':'22'}
print(a is b)   #a and b points to diffrent memory locations in the case of list even though their values are same

a=2.2   #float
b=2.2
print(a is b)'''

#  Q find average of 3 numbers
#operators precedence
a=1
b=2
c=3
sum=a+b+c
print(sum/3)