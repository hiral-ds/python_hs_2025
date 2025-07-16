class form:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} My id is {self.id}")

class form1:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} My id is {self.id}")    

Student1=form("Ishan",1)
print(Student1.admission())

Student2=form1("Akshu",2)
print(Student2.admission())     