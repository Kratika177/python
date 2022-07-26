import random
import math
i=0
user_score=0
computer_score=0
computer=["snake","water","gun"]

while(i<=10):
   print("1-SNAKE\n2-WATER\n3-GUN\n")
   user=int(input("Enter index of the following "))
   x=random.choice(computer)
   if (x=="snake" and user==2) or (x=="gun" and user==1) or (x=="water" and user==3):
       computer_score=computer_score+1
       print("computer wins this chance")
   elif (user==1 and x=="water") or(user==3 and x=="snake") or (user==2 and x=="gun"):
       user_score=user_score+1
       print("you wins this chance")
   i=i+1
if computer_score>user_score:
    print("Winner is computer")
elif(user_score>computer_score):
    print("Winner is you")
else:
    print("There is tie between both")
