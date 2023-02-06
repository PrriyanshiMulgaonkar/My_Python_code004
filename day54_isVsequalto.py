a=[1,2,3]
b=[1,2,3]

c=(3,4)
d=(3,4)
print(c is d)
print(a is b) #exact location of object in memory or having same identity
print(a==b) #value

x = "hello"
y = x
x += " world"
print(y)
