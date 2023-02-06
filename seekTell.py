f=open('myfile.txt','r')
print(type(f))
f.seek(10) #pointer will jump to 10 and then read the file

print(f.tell()) #this will show the current position of seek or pointer
data=(f.read(5))
print(data)

