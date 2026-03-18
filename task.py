fruits=["apple", "banana", "cherry", "mango"]
print(fruits)
fruits[1]="orange"  #replace
print(fruits)

fruits.append("grape")
print(fruits) #insert

fruits.remove('cherry')
print(fruits) #remove



text = "Python Programming"
print(text)
print(text[0:6])  #slicing

print(text[::-1])
print(text[-1:-12:-1]) #reverse

new_s=text.replace("Programming","language")
print(new_s) #replace

print(new_s.upper()) #uppercase



for i in range(0,4):
    for j in range(i):
        if(i==3):
            break
        print("*",end=" ")
    print("*")      
