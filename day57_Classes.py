class Person:
    name="Shubham"
    occupation="Software devloper"
    networth=10
    def info(self):
        print(f"{self.name} is {self.occupation}")
a=Person()
a.name="harry"
a.occupation="coder"

b=Person()
b.name="ritika"
b.occupation="HR"
print(a.name,a.occupation)
a.info()
b.info()