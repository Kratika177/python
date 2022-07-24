ch="y"
while ch=="y":
 n=int(input("Enter an Integer- "))
 c=int(input("Enter 1 or 0- "))
 if c==0:
    b=False
 if c==1:
    b=True
 if b==False:
   for i in range(0,n):
       for j in range(i,n):
           print("*",end="")
       print()
 if b==True:
   for k in range(0,n):
       for l in range(0,k+1):
           print("*",end="")
       print()
 ch=input("Enter y if you want to create more patterns and Enter n if you do not want to create more- ")
 if ch=="y":
     continue
 if ch=="n":
     break