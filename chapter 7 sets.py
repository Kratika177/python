s=set({1,2,3,4,5})
print("the type od variable s is= ",type(s))
print("The values in set s are= ",s)
#create set by list
list=[4,5,6,7,8,9]
s1=set(list)
print("values in set s1 are",s1)
print("Union of set s and s1 is",s.union(s1))
print("Intersection of set s and s1 is",s.intersection(s1))
s.remove(4)#element that is to be deleted
print("Set after deleting 4",s)
s1.add(10)
print("Set s1 after adding 10",s1)
print("Is set S and S1 are disjoint or not----",s.isdisjoint(s1))