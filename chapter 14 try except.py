n1 = input("Enter number 1= ")
n2 = input("Enter number 2= ")
try:
    print("Sum of number 1 and number 2 is",int(n1) + int(n2))
except Exception as e :
    print("ERROR =",e)