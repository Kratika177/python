var=0
while 1:
    if var<5:
        var=var+1
        continue
    print(var,end=" ")
    var=var+1
    if var>45:
        break
print("")
#quiz

while(1):
    if int(input("Enter a number= "))<100:
        continue
    else:
        print("finally you enter a number which is > 100")
        break