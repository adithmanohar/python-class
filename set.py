a={1,2,3,3,4,4,5,5} #set is mutable(we can change)
print(a)
print(set([5,5,6,6,7,7]))
emptyset=set()
print(emptyset)
emptyset={} # empty set cannot be created using {}
print(type(emptyset))

#accessing set items
print(2 in a) #true
print(9 in a) #false

#adding items
a.add(6)
print(a)
a.update([7,8,9,10])
print(a)

#removing items
a.remove(10)
print(a)
'''a.remove(15) #error
print(a) '''
a.discard(15)
print(a)

#joining items
b={1,12,13,4,5,2,14,15}
print(a.union(b))

#intersection
print(a.intersection(b)) #common elements edukulu

#set differnce
print(a-b) # fisrt setl illadum 2nd setil illathadhum ayaa elements print cheyu
print(b-a) #second setl illadum 1st setil illathadhum ayaa elements print cheyu

#symmetric diiference
print(a^b) #common ayaa elements ne print cheyilaa(2lum unique aya elements print cheyu)

#frozenset
c=frozenset(b)
print(c)
'''print(c.add(4)) ''' #we cannot add elements to frozenset
set1={1,2}
set2={1,2,3,4}
print(set2.issuperset(set1))
