#we have to print alternate items by using enumerate functions

l1= ["aloo","bhindi","chole","Rajma"]
for index , items in enumerate(l1):
    if index % 2==0:
        print(f"You have to buy {items}")
