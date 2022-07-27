import time
initial=time.time()
#while loop
k=0
while(k<5):
   print(f"you are in while loop -iteration({k+1})")
   k+=1
   time.sleep(2)
print(f"Time taked to run while loop 50 times is {time.time()-initial} secs")
print()

#for loop
initial2=time.time()
for i in range(0,5):
    print(f"you are in for loop -iteration({i+1})")
print(f"Time taked to run while loop 50 times is {time.time()-initial2} secs")

print(f"current time is {time.asctime(time.localtime(time.time()))}")