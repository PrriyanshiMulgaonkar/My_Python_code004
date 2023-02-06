class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"The employee name is {self.name} and id is {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("Default language is Python")
e=Employee("Rohan",23)
e.show()
e1=Programmer("Harry",4100)
e1.showLanguage()