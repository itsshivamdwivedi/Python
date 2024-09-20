#acces modifiers in python
# three types of the modifiers that is public , private and protected modifiers 
                       # public modifiers
# class Employee:
#     def __init__(self):
#         self.name = "name"
        
# a= Employee()
# print(a.name)
# this is an example of the public modifiers as we can access this from anywhere 

#####    THe second type of the modifiers is private modifiers we can private it using __ double underscore.
                               # private modifiers
# class Employee:
#     def __init__(self):
#         self.__name = "acer"
        
# a= Employee()
# # print(a.__name) 
# # this cannot be accesed as it is private modifiers
# print(a._Employee__name)
# # to acces this we can use name mangling method 
# print(a.__dir__()) this shows all the directories from which we can use the name mangling method _Employee__name is one amongst these

                           # protected modifier


