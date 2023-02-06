# map
def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,4,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))

d=list(map(cube,l))
print(newl)
print(d)

# filter
def filter_func(a):
    return a>2

newnewl=list(filter(filter_func,l))
print(newnewl)

# reduce
from functools import reduce
num=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)