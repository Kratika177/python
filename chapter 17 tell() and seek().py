f=open("sample.txt")
#tell function will you that at which character the curser is currently now.
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
#seek function is use to reset the curser whereever we want by providing the index
f.seek(0)
print(f.tell())