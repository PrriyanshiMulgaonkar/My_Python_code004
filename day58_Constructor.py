class person:
    def __init__(self,n,o):
        print("Constuctor called")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=person("Harry","devop")
b=person("di","HR")
a.info()
b.info()