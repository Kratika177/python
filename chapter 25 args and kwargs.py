# *args is used when we have to udate the parameters rapidly so instead of doing it all over just use *args method
def func(nor,*args,**kwargs): #we can use the normal parameters with *args
    print(nor)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"square of {key} is {value}")

items=[1,2,3,4,5,6]
kw={"1":"1","2":"4","3":"9","4":"16","5":"25","6":"36"}
func(0,*items,**kw)
