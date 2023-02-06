x=5
def wel():
    global x #function to change the global variable
    x=6
    y=10
    print(x)
    print(y)
print(x)
wel()