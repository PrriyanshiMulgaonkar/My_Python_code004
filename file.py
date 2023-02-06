# f=open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()

# f=open('myfile.txt','w')
# f.write("hello3")
# f.close()

with open('myfile.txt','a') as f:
    f.write(" heyyyyy")