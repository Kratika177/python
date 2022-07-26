x=10 #global variable
def func1():
    #x=6 #Local variable
    global x #we have to write this in order to modify the global variable
    x=x+6 #we cannot modify local variable directly like this
    print("x=",x)
func1()    