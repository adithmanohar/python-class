#single interface/(sAME PER) multiple implimentation(definison)
"""
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
"""
#question1
"""
: Write a Python program to demonstrate Polymorphism using classes
Bird , Parrot , and Sparrow .
Requirements:
1. Create a base class Bird with a method sound() that prints "Bird makes a sound" .
2. Create two subclasses:
Parrot → Overrides sound() to print "Parrot says 'Hello'"
Sparrow → Overrides sound() to print "Sparrow chirps"
3. Define a function make_sound(bird) that calls the sound() method of the object
passed.
4. Create objects of Parrot and Sparrow and pass them to make_sound() .

Sample Output:
Parrot says 'Hello'
Sparrow chirps
"""

class Bird:
    def sound(self):
        print("Bird makes a sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says 'Hello'")
        
class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")


def make_sound(bird):
     bird.sound()


parrot1=Parrot()
sparrow1=Sparrow()

make_sound(parrot1)
make_sound(sparrow1)