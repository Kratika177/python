#indexing of the the string in python start from 0

mystr= "This is a sample code for string slicing"
print(mystr)
print(mystr[0:4]) #the ending index must be one more than till the index you want to print
print()

#to print alternate characters
print("print alternate characters----")
print(mystr[0:len(mystr)+1:2]) #last argument is jump factor
print()

#if we donot specify the ending index then it will print till the end
print("if we donot specify the ending index then it will print till the end----")
print(mystr[0:])
print()

#if we donot specify the starting address then it will assume start index as 0
print("if we donot specify the starting address then it will assume start index as 0----")
print(mystr[:4])
print()

#if we donot specify any start or end index then it will assume start index as 0 and end as the len+1
print("if we donot specify any start or end index then it will assume start index as 0 and end as the len+1----")
print(mystr[:])
print()

#if we donot specify the jump factor then it will assume it as 1
print("if we donot specify the jump factor then it will assume it as 1----")
print(mystr[0:len(mystr)+1:])
print()

#if we take negative index it means that we have to scan from the end last char is -1 and so on
print("if we take negative index it means that we have to scan from the end last char is -1 and so on----")
print(mystr[::(-1)])
print()

#FUNCTIONS

# 1- .isalnum()
print(mystr.isalnum())

# 2- .capitalize
print(mystr.capitalize())

# 3- .find
print(mystr.find("slicing"))

# 4- .count
print(mystr.count("i"))

# 5- .endswith
print(mystr.endswith("g"))

# 6- .islower
print(mystr.islower())

# 7- .replace
print(mystr.replace("is","are"))