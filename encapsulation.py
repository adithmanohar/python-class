#protcting data

class Employee:

   
    def __init__(self,name1,salery2):
      self.name=name1  #public atribute
      self.__salery=salery2 #privte attribute
    def displayemployee(self):
         print(self.name)
         print(self.__salery)
    def updatesalery(self,newsalery):
        self.__salery=newsalery    

emp=Employee("adith",200)
print(emp.name)
emp=Employee(100,"adith")
#print(emp.__salery)      we cant print it is private
emp.updatesalery(500)
emp.displayemployee()
