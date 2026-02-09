#creating a dictionary   (we can change dictinoary(mutable))
ab={'name':'adithmanohar','age':22,'rollno':2}
cd=dict(name='adith',age=2,rollno=23)
print(cd)
print(ab)
#accessing elements

print(cd['age'])
print(ab.get("age"))

#updating dictionary
ab['age']=30
print(ab)
#adding items
ab['mark']=60
print(ab)

#removing items
ab.pop('age')
print(ab)
print(ab.popitem())#it removes the last keyvalue pair
#nested dictionary

college={"student1":{'name':'adithmanohar','age':22,'rollno':2},
         "student2":{'name':'adith','age':2,'rollno':22},
         "student3":{'name':'adithm','age':24,'rollno':23}
         }
print(college)
print(college['student2'])

#dict(ionary methods
a={'name':'ram','age':22,'rollno':2}
print(a.keys())
print(a.values())
print(a.items())
school={'name':"jhon",'age':30}
school.update({"city":'newyork',"age":31})
print(school)
#from keys

keys=["color","weight","height"]
print( dict.fromkeys(keys,"unknown")) #creating a dictionary useing from key method
newdict=dict.fromkeys(keys,"unknown")
newdict["color"]="red"
print(newdict)



