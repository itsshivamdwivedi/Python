#local variable and global variable in python 
x = 4 

def my_function():
  global x 
  x=45
  print(x)
my_function()
print(f"The value of x in global variable is {x}")
    