# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b
# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# # print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
# my_list = [i for i in range(-1, 2)]
# print(my_list)
# def func_1(a):
#    return a ** a


# def func_2(a):
#   return func_1(a) * func_1(a)


# print(func_2(2))
# def any():
#    print(var + 1, end='')


# var = 1
# any()
# print(var)
# def fun(inp=2, out=3):
#     return inp * out
 
 
# # print(fun(out=2))
# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']
 
# for k in range(len(dictionary)):
#     v = dictionary[v]
 
# print(v)
# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# try:
#    value = input("Enter a value: ")
#     print(value/value)
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")
# my_list = ['Mary', 'had', 'a', 'little', 'lamb']
 
 
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
 
 
# print(my_list(my_list))
# nums = [1, 2, 3]
# What is the output of the following piece of code if the user enters two lines containing 2 and 4 respectively?

# x = float(input())
# y = float(input())
# # print(y ** (1 / x))
# # # vals = nums
# # # del vals[:]
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)
 
 
# print(fun(0, 3))
# # How many stars (*) will the following snippet send to the console?
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)
 
# # i = 0
# # while i < i + 2 :
# #     i += 1
# #     print("*")
# # else:
# #     print("*")
# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#    print(x, end="")
# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#    print(dct[x][1], end="")
# def fun(inp=2, out=3):
#    return inp * out


# print(fun(out=2))
# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#    for c in range(3):
#       if lst[r][c] % 2 != 0:
#        print("#")
# What is the expected behavior of the following program?

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
    # print("Too bad...")
# foo = (1, 2, 3)
# foo.index(0)
print("Hello, World!")







