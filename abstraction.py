from abc import ABC,abstractmethod  #hdiding the implimentaion and show essential details
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,width,height):
     self.wd=width
     self.ht=height
    def area (self):
        return self.wd*self.ht
    
class Circle(Shape):
    def __init__(self,rd):
     self.radius=rd
    def area (self):
         return 3.14*self.radius*self.radius
  
#shape1=Shape()   #error
rectangle1=Rectangle(4,5)
print(rectangle1.area())
circle1=Circle(5)
print(circle1.area())