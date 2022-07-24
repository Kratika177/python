def average(list):
    for item in list:
        sum = 0
        sum = sum+int(item)
    avg = sum / len(list)+1
    print("Average is= ",avg)
l=[]
n = int(input("Enter the number of numbers of which u want to calculate average= "))
for x in range(0,n):
    ele = int(input("Enter the number= "))
    l.append(ele)
average(l)
