# #in this file we are going to learn the constructors in python
# class person:
#     def __init__(self, name,occ):
#         self.name = name
#         self.occ=occ
#
#     name = "shivam"
#     occ ="chor"
#     def info(self):
#         print(f"{self.name} is a {self.occ}") 
#
# a = person("harry","Developer")
# b = person("Divya","HR")
# a.info()
# b.info()
class Mathes:
    a=10
    def __init__(self):
        print("shivam")
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print("my name is shivam")
        print(a+b)
obj=Mathes()

obj.showvalue()
obj.showvalue1(20,30)