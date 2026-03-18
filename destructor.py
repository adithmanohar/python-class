#to delete
"""
class Person:
    def __init__(self,name,age):
        self.name1=name
        self.age1=age
        print(self.name1)
        print(self.age1)
    def __del__(self):
        print(f"{self.name1}and{self.age1}deleted")


person1=Person("adith",22)

del person1
print(person1.name1)
print(person1.age1)

"""

#class variables vs insatnce varaibles

class Student:
    schoolname="ABC high school" #class variable
    def __init__(self,name,grade):
          self.name1=name #instance varaible
          self.grade1=grade

student1=Student("adith",22)
print(Student.schoolname)
print(student1.name1)
print(student1.grade1)
