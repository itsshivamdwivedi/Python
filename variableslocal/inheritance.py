class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show_details(self):
        print(f"The name of the employee:{self.id} is {self.name}")
class programmer(Employee):
    def showlanguage(self):
        print("The default programming language is python")
e1 = Employee("xyz",400)
e1.show_details()
e2=programmer("harry",430)
e2.show_details()
e2.showlanguage()