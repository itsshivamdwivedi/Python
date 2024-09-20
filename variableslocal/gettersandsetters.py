#getters and setters in python
#underscore after self indicates that it is private
# below code is an example of the getters 
# class car:
#     def __init__(self):
#      self._color="red"
#     def get_color(self):
#         return self._color 
# my_car = car()
# print(my_car.get_color())
# print(my_car.color)
# my_car.color ="blue"
# print(my_car.color)
# by this way we can control how the color is accessed 
# we can add  some rules and regulations by getters and setters
   # setters 
# class Car:
#     def __init__(self):
#         self._color="red"

#     def get_color(self):
#         return self._color
#     def set_color(self, new_color):
#         self._color=new_color
        
# my_car = Car()
# my_car.set_color("blue")
# print(my_car.get_color())

# we can also add some functionality to our code by using the getter and setters .
# for example we want to validate some new color before setting it we can do it using the getters and setters 
class car:
    def __init__(self):
        self._color = "red"
        
    def get_color(self):
        return self._color
    def set_color(self,new_color):
        if new_color in ["red","blue","green"]:
           self.color= new_color
        else:
            print("Invalid color!")
        
        
my_car = car()
my_car.set_color("yellow")
print(my_car.get_color())