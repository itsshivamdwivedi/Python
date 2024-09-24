# With the break statement we can stop the loop before it has looped through all the items:
# a =["mango", "banana","orange"]
# for i in a :
#     if a == "banana":
#      break
#      print(a)
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")
#if the loop breaks then the else block is not executed

# how to print each objective for every fruit 
fruits = ["Apple", "Banana","mango"]
adj= ["red","big","tasty"]
# for x in adj:
#     for y in fruits:
#         print(x,y)

# If we want to iterate both the lists simultaneously we have zip method
for x,y in zip(adj,fruits):
    print(x,y)



# how to print the table from 1 to 10 using the for loop 
# for i in range (1,11):
#     print("table of",i)
#     for j in range (1,11):
#         print(i,"x",j,"=",i*j)
#         print()
#write
# range(1,6)
# for n in range(1,6,2):
#     print(n)
# for a in range(1,11):
#     print("2*",a,"=",2*a)
#     # how to reverse the number or element we use -1
# # for a in range(10,0,-2):  reverse table
#     print("2*",a,"=",2*a)