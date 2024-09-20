# local variable and global variable in python
x = 4
def  my_function():
    global x
    x = 5
    print(x)
my_function()
print(f"The value of the global variable x is changed to {x}")
