list=["item1","item2","item3","item4"]
print("list is- ",list)
print("First element in the list is- ",list[0])
print("first three element of list is- ",list[0:3])
print("alternate members of list is- ",list[::2])
print("reverse of the list is- ",list[::-1])
list[0]="item0"
print("list after changing first ellement is- ",list)  #list is muttable means we can change the elements of the list
print()

#if we want to create a list whose element cannot be changed then we must use tuple
tuple1=("item1","item2","item3","item4")
print("tuple is- ",tuple1)
#tuple1[0]="item0" #this will give error because tuples are immutable

#to sort the list
list.sort()
print("sorted list= ",list)


list.append("item5")
print(list)
