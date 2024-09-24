#  Two types of typecasting implicit and explicit 


#  Implicit typecasting is built in and python converts the datatypes by itself 

a=10
 #type of a is <int>
b=7.3    
#type of b is <float>
c="shivam"
#type of c is <class 'str'>

# Explicit Typecasting  involves the user to convert the datatype to the required datatype
# This type of typecasting can be done with these datatypes int float and str

#Example:-
a=5

# b=float(a)  
b=str(a)   #it converts the int to string
print(b)
print(type(b))