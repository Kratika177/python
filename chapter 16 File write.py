f=open("sample.txt","r+")
f.write("\nexternally added text\n")
print(f.read())
f.close()