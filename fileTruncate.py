with open('sample.txt','w') as f:
    f.write("Hello world")
    f.truncate(5) #to write only 5 character in file

with open('sample.txt','r') as f:
    print(f.read())