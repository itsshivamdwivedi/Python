# IN python there are three built in functions
# x=[1,2,3] this is list 
x =(2,3,4)
print(dir(x))
print(x.__add__)
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
p = Person("John",34)
print(p.__dict__)
print(help(Person))