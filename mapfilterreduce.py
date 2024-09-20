def cube(x):
    return x*x*x 
# print(cube(3))
l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# newl =list(map(cube,l))
# apart from writing cube in a function we can also do it by using a lambda function
newl = list(map(lambda x: x*x*x, l))
print("This is an example of map function",newl)
# this is an example of the map function 

# filter
def my_filterfunc(x):
    return x>100
updatedlis = (list(filter(lambda x:x*x*l)))
print(updatedlis)
#reduce
from functools import reduce
def mysum(x,y):
    return x*y
sum = reduce(mysum,l)
print(sum)