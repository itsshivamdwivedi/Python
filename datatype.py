# l=[223,45]
# l[1]="shivam"
# print(l)
# # lists are mutable and we can change and edit the lists
# # t=(10)  this is not a tuple because there is not more than one element inside the round bracket .
# # t=(10,20,30)  this is tuple as the element are in round bracket and separated by the commas
# # print(t,(type(t)))
# # dictionary always have key and value pairs and it is mostly used in the database to seek data
# d={
#     "name":"shivam" ,"course":"python"
# }
# print(d["name"])
# # set is also immutable
# # s=()
# # the another property of the set is that it takes repeated element at once
# # print(s(type(s)))
# s1=set([2,3,2,4,5])
# print(s1,type(s1))
# s ={10,20,30,10}
# print(s,type(s))

# <<<<<<< HEAD
# a ={2,3,"shivam"}

# # An empty dictionary is a set 
# print(a,type(a)) 
# =======


# reverse a string using for loop and functions
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("hello Shivam "))

#  Method Number 2 for reversing a  string
# def reverse_string(str):
#     reversed_string =""
#     for i in range(len(str)):
#         reversed_string = str[i] + reversed_string

#     return reversed_string

# str="Hii I am Shivam"
# print("The reversed String is ",(reverse_string(str)))


# def reversing_string(str):
#     reversed_string=""
#     for i in range(len(str)-1,-1,-1):
#         reversed_string += str[i] 

#     return reversed_string


# str ="Hello My name is shivam"
# print("The reversed String is" ,(reversing_string(str)))

# str=input("Enter Your name ")
# print("Good Afternoon",(str))

# Detecting space in python
# str =" "
# s=str.isspace()      #output: True
# print(s)

#  Removing the whitespace from the starting and ending of the string using python
# a ="     MY name is shivam     "
# b=a.strip()
# print(a)
# print(b)  #output: Mynameisshivam
# #  To remove the white space from overall string from anywhere we can use replace method
# c=a.replace(" ","")
# print(c)


























#   list in Python is another datatype
# lst=["Hello","My nam is",1,"shivam",2,3,5,6,7,8]
# print(lst)
# print(type(lst))

# #  List Slicing method in python
# print(lst[2:9:3])
# # It works on the following format [Initial:End:IndexJump]
#                                 #    [2:9:3]
# # Reversing a list using slicing method 
# print("The reversed list is ",lst[::-1])







#  Reversing a list using function

# def reverseing_list(lst):
#     reversed_list = []
#     for i in range(len(lst)-1,-1,-1):
#         reversed_list.append(lst[i])
#     return reversed_list


# lst=["Hello","My nam is",1,"shivam",2,3,5,6,7,8]
# print("The reversed list using for loop is ",(reverseing_list(lst)))