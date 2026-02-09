s="hello world"
#slicing
print(s[0:7])
print(s[-1])
print(s[-5:])
print(s[7:])
print(s[:7])
print(s[7])      
print(s[-11:])
print(s[-7:])
print(s[-7:-2])
print(s[:-2])
print(s[:])
print(s[:-11])
print(s[1:-7])

#skipping characters
print(s[0:5:2])
print(s[0:5:4])

#reversing a string
print(s[::-1])
print(s[::2])
print(s[::4])
print(s[::-5])

#modifying strings
new_s=s.replace("world","python")
print(new_s)
print(s.replace("ll","l"))
print(s.upper())
print(s.lower())

#string concatenation
a="ADITH"
b="MANOHAR"
c="M"
print(a+" "+ b+" " +c+" " )
a="ADITH"
b="10"
print(a+b)

a="ADITH"
b="MANOHAR"
c="M"
print(a+","+b+" ,"+c)

#format string
name="manohar"
age=22
print("my name is {} and i am {} years old".format(name,age)) #method1

print("my name is {n} and i am {a} years old".format(n="adithmanohar",a=22)) #method2

formatted_string ="my name is {n} and i am {a} years old".format(n="adithmanohar",a=22)
print(formatted_string) 

d="adithmanohar"
e=22
print(f"my name is {d} and i am {e} years old") #method3 simple way(using f sting)

#escape charcters
print("adith")
print("manoahr")
print("adith\nmanohar") #newline jump
print("adith\tmanohar") #space varum
print("adith'manohar'") #dont use same quats

#string methods
print(len(s))
a= " my name, is adith "
print(a.strip())#removes starting and ending spaces
print(a.split(",")) #splitting elements of a string
print(s.find("world"))
s="hello world world"
print(s.find("world"))#returns first index
print(s.count("World"))#to count
print(s.startswith("hello"))

print(s.endswith("hello"))


print(s[4])

s[6]="A"#error string elements cannot be modifyed
print(s)


