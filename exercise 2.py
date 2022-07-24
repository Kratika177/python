#faulty calculator
#45*3=555, 56+9=77, 56/6=4

operator=input("Enter the operator-- ")
num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
if(operator== "+"):
    if (num1==56 and num2==9):
        print("56 + 9 = 77")
    else:
        print(num1,"+",num2,"=",num1+num2)
if(operator== "*"):
    if ((num1==45 and num2==3) or (num1==3 and num2==45)):
        print("45 * 3 = 555")
    else:
        print(num1,"*",num2,"=",num1*num2)
if(operator== "/"):
    if num1==56 and num2==6:
        print("56 / 6 = 4")
    else:
        print(num1,"/",num2,"=",num1/num2)

if(operator=="-"):
    print(num1, "-", num2, "=", num1-num2)