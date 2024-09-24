# Reversing methods for all datatypes 

# String reverse using for loops

# def reverse_string(str):
#     reversed_str = ""
#     for i in str:
#         reversed_str = i + reversed_str
#     return reversed_str

# str="My name is Shivam"
# print("The Original string is ",(str))
# print("The reversed string is",(reverse_string(str)))

#  Method 2 to reverse the string in python using for loop 

# def reverse_string(str):
#     reversed_str = ""
#     for i in range(len(str)-1,-1,-1):
#         reversed_str+= str[i]
#     return reversed_str  # returning the variable reversed_str

# str="My name is shivam"

# print("THe new reversed string is",(reverse_string(str)))

def reverse_str(str):
    str =str[::-1]
    return str

str = "My name is shivam"
print("The reversed string is ",(reverse_str(str)))



#  Reversing the lists using For loops

def reverse_list(lst):
    reversed_lst = []
    for i in range (len(lst)-1,-1,-1):
        reversed_lst.append(lst[i])
        
    return reversed_lst

lst=['shivam',"Eats","Big Mango"]
print("The current list is ",(lst))
print("The reversed  list is ",(reverse_list(lst)))


# Reversing a dictionary using for loops with python

# def reverse_dictionary(dict):
#     reversed_dictionary = {}
#     for i in range (len(dict)-1,-1,-1):
#         reverse_dictionary.append(dict{dict})


    
     



        
