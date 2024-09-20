# args take the argument as a tuple
# **kwargs take the argument as a dictionary as a key value pairs
#why should we use decorators 
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thank you")
    return mfx

@greet
def hello():
    print("HEllo world") 
    
@greet
def add(a,b):
    print(a+b)
    
hello()
add(1,2)