a=(1,2,3,4,5)
#accessing tuple items
print(a[3])
print(a[1:4])

#updating a tuple
'''a[3]=6
print(a)#error  we  cannot edit tuple '''
new=list(a)
new[3]=6
print(tuple(new))

#joiningtuple
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)

#tuplemethods
print(tuple1.count(2))
print(tuple1.index(3))
#del tuple1
#print(tuple1) #error

#adding elements to tuple
print(tuple2+(7,8,9))
newtuple=tuple1+tuple2+(7,8,9)
print(newtuple)

#using list
new=list(tuple1)
new.append((11,22,33))
newtuple=tuple(new)
print(newtuple)
#print(type(newtuple))