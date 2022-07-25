def getdate():
    import datetime
    return datetime.datetime.now()
def data_input():
    choice="y"
    while(choice=="y"):
     print("Your clients are-\n1-Rohan\n2-Harry\n3-Hammad")
     c=int(input("Enter the index of the client of which you want to lock the information- "))
     if(c==1):
        d=int(input("Enter the index of data you want to enter-\n1- Diet\n2- Exercise\n"))
        if(d==1):
            with open("rohan_diet.txt","a") as f:
                ch="y"
                while ch=="y":
                    print("write your diet- \n")
                    s=input()
                    dt = str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch=str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch=="y":
                        continue
                    else:
                        break
        if (d == 2):
            with open("rohan_exercise.txt", "a") as f:
                ch = "y"
                while ch == "y":
                    print("write your exercise- \n")
                    s = input()
                    dt = str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch = str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch == "y":
                        continue
                    else:
                        break
     if (c == 2):
        d = int(input("Enter the index of data you want to enter-\n1- Diet\n2- Exercise\n"))
        if (d == 1):
            with open("Harry_diet.txt", "a") as f:
                ch = "y"
                while ch == "y":
                    print("write your diet- \n")
                    s = input()
                    dt = str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch = str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch == "y":
                        continue
                    else:
                        break
        if (d == 2):
            with open("Harry_exercise.txt", "a") as f:
                ch = "y"
                while ch == "y":
                    print("write your exercise- \n")
                    s = input()
                    dt = str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch = str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch == "y":
                        continue
                    else:
                        break
     if (c == 3):
        d = int(input("Enter the index of data you want to enter-\n1- Diet\n2- Exercise\n"))
        if (d == 1):
            with open("hammad_diet.txt", "a") as f:
                ch = "y"
                while ch == "y":
                    print("write your diet- \n")
                    s = input()
                    dt = str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch = str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch == "y":
                        continue
                    else:
                        break
        if (d == 2):
            with open("hammad_exercise.txt", "a") as f:
                ch = "y"
                while ch == "y":
                    print("write your exercise- \n")
                    s = input()
                    dt=str(getdate())
                    f.write("["+dt+"] "+s+"\n")
                    ch = str(input("Want to enter more enteries? enter y for yes and n for no- "))
                    if ch == "y":
                        continue
                    else:
                        break
     pl=input("Do you want to enter data of more clients? enter y for yes and n for no- ")
     if(pl=="y"):
         continue
     else:
         break

def data_display():
    print("You can view the data here, your clients are\n1-Rohan\n2-Harry\n3-Hammad\n")
    cli=int(input("Enter the index of client whose data you want to display\n"))
    data = (int(input("Enter data you want to display\n1-diet\n2-exercise")))
    if cli==1:

        if data==1:
            with open("rohan_diet.txt") as f:
                content=f.read()
                print(content)
        if data==2:
            with open("rohan_exercise.txt") as f:
                content = f.read()
                print(content)
    if cli==2:
        if data==1:
            with open("Harry_diet.txt") as f:
                content = f.read()
                print(content)
        if data==2:
            with open("Harry_exercise.txt") as f:
                content = f.read()
                print(content)
    if cli==3:
        if data==1:
            with open("hammad_diet.txt") as f:
                content = f.read()
                print(content)
        if data==2:
            with open("hammad_exercise.txt") as f:
                content = f.read()
                print(content)
data_input()
data_display()