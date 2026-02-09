a=int(input("enter a number"))
b=input("enter a operator + - / * ")
c=int(input("enter a number"))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
    
elif b=="/":
    if   c!=0:
        print(a/c)     
    else:
        print("cannot divided by zero")
else:
    print("invalid number")