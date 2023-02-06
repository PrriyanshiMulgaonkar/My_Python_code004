class employee:
    def __init__(self):
        self.__name="Rohan"
a=employee()
# print(a.__name) #cannot access directly
# name mangling
print(a._employee__name) #can be access indirectly
print(a.__dir__())

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "Code"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())