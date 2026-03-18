#class #(plan)

class Dog:
    def __init__(self,nm,bd): #fileds ne intilize cheya
        self.name=nm #fileds
        self.breed=bd
    def bark (self):
        print(f" {self.name} says woof")

        #create object

dog1=Dog("rocky","pug")
dog1.bark()
print(dog1.breed)
print(dog1.name)
dog2=Dog("abc","bcd")
dog2.bark()
print(dog2.breed)
print(dog2.name)

