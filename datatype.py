l=[223,45]
l[1]="shivam"
print(l)
# lists are mutable and we can change and edit the lists
# t=(10)  this is not a tuple because there is not more than one element inside the round bracket .
# t=(10,20,30)  this is tuple as the element are in round bracket and separated by the commas
# print(t,(type(t)))
# dictionary always have key and value pairs and it is mostly used in the database to seek data
d={
    "name":"shivam" ,"course":"python"
}
print(d["name"])
# set is also immutable
# s=()
# the another property of the set is that it takes repeated element at once
# print(s(type(s)))
s1=set([2,3,2,4,5])
print(s1,type(s1))
s ={10,20,30,10}
print(s,type(s))

a ={2,3,"shivam"}

# An empty dictionary is a set 
print(a,type(a)) 