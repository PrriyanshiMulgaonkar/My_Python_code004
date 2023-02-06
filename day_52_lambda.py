def apply(fx,value):
    return 6+fx(value)

double=lambda x: x*2
cube=lambda x: x*x*x
average=lambda x,y:(x+y)/2
print(double(2))
print(cube(2))
print(average(3,3))

print(apply(cube,2))
print(apply(lambda x:x*x*x,2))