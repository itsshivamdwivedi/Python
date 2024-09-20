# Encapsulation method
class Student:
          def __init__(self, name):
                  self.__name =""
          def getname(self):
                  return self._name
           def setname(self,name):
                self._name=name

obj=Student()

obj.setname("Testing")
name=obj.getname()
print(name)
# We use getters and setters when we have to set the value privately and call it through the object
