a=int(input("enter a number"))
b=input("enter a operator + - / * ")
c=int(input("enter a number"))
if b=="+":
    print(f"result {a+c}")
elif b=="-":
    print(f"result {a-c}")
elif b=="*":
    print(f"result {a*c}")
    
elif b=="/":
    if   c!=0:
        print(f"result {a/c}")     
    else:
        print("cannot divided by zero")
else:
    print("invalid number")