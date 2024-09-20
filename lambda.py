print("Hello world")
# def double(x):
#     return x*2
# print(double(5))
#  the above same problem can be wruteen using lambda function
def appl(fx,value):
    return 6+fx(value)
double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3
print(appl(lambda x:x*x*x,2))
print(appl(cube,2))
print(double(3))
print(cube(3))
print(avg(3 ,5 ,10))
