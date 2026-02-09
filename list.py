a=[1,2,3,4]
print(a)
#accessing list items

print(a[2])
print(a[1:4])
#changing list items

a[2]=5
print(a)
a[3]="apple" #list is mutable(change cheyan pattum)
print(a)
#changing multiple elements

a[1:3]=True,False
print(a)
#adding item to list


a.append("red")
print(a)
a.insert(1,"hello")
print(a)
b=[1,1.2,True,"red"]
a.extend(b)
print(a)
#removing items from list

a.remove("apple")
print(a)
print(a.pop(2))
print(a)

del a[0]
print(a)

'''del a #to clear element with index and also we can delete entire list
print(a)'''
a.clear()# to clear element
print(a)

#list methods

c=[1,2,2,3,3,3]
print(c.count(2))
print(c.index(2))
c.reverse()
print(c)
#sorting a list

c.sort()
print(c)
c.sort(reverse=True)
print(c)

#joining lists

list1=[1,2,3,4,5,6]
list2=[7,8,9]
print(list1+list2)
