var1="string "
var2="second string"
var3= 45
var4= 56.7
var5="56"
var6="87"

#knowing the type of the variable

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#using "+"

print(var3+var4) #var3 and var4 both are numbers so they will add
print(var1+var2) #var1 and var2 both are string so they will concatinate

#typecasting

print(int(var5)+int(var6))

#taking input

print("enter the number")
num=input() #it take input and store in variable num in string format
print("you entered ",num)

#adding two numbers
print("enter number 1")
num1=input()

print("enter number 2")
num2=input()

num3=int(num1)+int(num2)
print("sum of number 1 and 2 is = ",num3)