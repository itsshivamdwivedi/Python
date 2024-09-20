# class method as tghe alternative constructors in python 
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], string.split("-")[1])
        
e1=Employee("Harry",1200)
print(e1.name)
print(e1.salary)
string ="xyz-12000"
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    @classmethod
    def fromstr(cls,string):
        name,age = string.split(",")
        return cls(name,int(age))
Person =Person.fromstr("Shivam salaray is ,30")
print(Person.name,Person.age)