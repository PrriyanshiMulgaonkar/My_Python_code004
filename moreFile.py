# f=open('myfile2.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=(line.split(",")[0])
#     m2=(line.split(",")[1])
#     m3=(line.split(",")[2])

#     print (f"Marks of {i} in maths is: {m1}")
#     print (f"Marks of {i} in maths is: {m2}")
#     print (f"Marks of {i} in maths is: {m3}")
#     print(line)

f=open("myfile3.txt",'w')
line=['line 1\n','line2\n','line3\n']
f.writelines(line)
f.close()