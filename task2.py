a=('apple', 'banana', 'cherry')
print(a)
b=list(a)
b[1]='orange'
print(b) #replace

tuple1=(1,2,3,)
print(tuple1[2])
print(tuple1[:])

#set
a={1,2,3}
a.add(4) #add
print(a)
a.update([5,6])#update
print(a)
b = {1, 2, 3}
c = {3, 4, 5}
print(b.union(c)) #union
print(b.intersection(c)) #intersection
print(b^c) #symmetric difference

