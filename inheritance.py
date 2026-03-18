"""
class Animal:
     

     def __init__(self,names):
          self.name=names
     def sound (self):
          print(f" {self.name} makes sound")
class Dog(Animal):
     def __init__(self,name,color):
          super().__init__(name)   # call parent constructor
          self.colors=color
     def strech(self):
        print(f" {self.name} can strech")

animal1=Animal("dog",)
animal1.sound()

dog1=Dog("pug","black")
dog1.sound()

dog2=Dog("dog","white")
dog2.strech()

print(dog1.colors)
print(dog2.colors)

"""

#multiple inheritance
"""
class Engine:
     
     def startEngine(n):
     
      print("Engine started")
class Wheels:
    def rotate(a):
        print("wheels are roatating")
class Car(Engine,Wheels):
     def drive(b):
       print('the car is driving')

car1=Car()
car1.startEngine()
car1.rotate()
car1.drive()
"""

#Hierarchical inheritance

#multiple child class can inhert single parent class

class Animal:
     def speak(a):
          print("animal can speak")
class Dog(Animal):
     def speak(b):
          print("dog barks")
class Cat(Animal):
     def speak(c):
          print("cat meows")

animal1= Animal()
dog1=Dog()
cat1=Cat()

animal1.speak()
dog1.speak()
cat1.speak()



