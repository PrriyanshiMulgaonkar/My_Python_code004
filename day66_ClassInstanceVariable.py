class Employee:
    # class variable
    companyName = "Apple"
    noOfEmp=0

    def __init__(self, name):
        self.name = name
        # instance variable
        self.raiseAmount = 0.3
        Employee.noOfEmp +=1

    def show(self):
        print(
            f"The name is {self.name} and raise amount is {self.raiseAmount} in {self.companyName} and no of emp is {self.noOfEmp} ")


emp = Employee("Henry")
emp.raiseAmount = 1
emp.companyName = "Apple India"
emp.show()

emp2 = Employee("Rasy")
emp2.show()
