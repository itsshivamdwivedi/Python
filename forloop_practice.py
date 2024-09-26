#  write a program in python that takes a list of strings and creates a new string that contains the lengths of each string

# words=["hello","Shivam","How","redmi"]
# lengths=[]
# for word in words:
#     lengths.append(len(word))
# print(lengths)


#  Write a program to print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

#  let's define the number of rows
# rows=5
# for i in range(1,rows + 1,1):

#     for j in range(1,i+1):          #inner loop 
#         print(j, end=" ")

#     print(" ")


# WAP In python to calculate the sum of all numbers from 1 to a given number entered by the users

# number=int(input("Enter a number"))
# sum=0
# for i in range(1,number+1):
#     sum+=i
    
# print(f"Sum of all numbers from 1 to {number} is {sum}")

# Write a program to get the multiplication table of number given by the user

# n=int(input("Enter a number of which you want multiplication table of"))

# for i in range(1,11,1):
#     product=n*i
#     print(f"{n} x {i} = {product}")

# write a program to display the numbers fron the lists using loop 

# numbers=[12,75,150,145,525,50]
# for number in numbers:
#     if number >500:
#         break
#     elif number>150:
#         continue
#     elif number %5==0:
#         print(number)

# Write a program to count the total number of digits in a number

# number=int(input("Enter a number"))
# count=0
# while number!=0:
#     number=number//10
#     count=count+1

# print("The total digits are",count)



# Print the reverse of the numbers using for loop 

# for num in range(10,0,-1):
#     print(num)
# Print the 1st 10 natural numbbers using for loop 
# for num in range(1,11):
#     print(num)


# Write a program to print the pyramid of the pattern

# rows=int(input("Enter the number of rows"))

# for i in range(1,rows+1,1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")

# Enter the number of rows6
# *
# **
# ***
# ****
# *****
# ******

# Simple Number pattern using for loop 

# rows=int(input("Enter the number of rows"))
# for i in range(1,rows+1):             #outer loop handle the number of rows
#     for j in range(1,i+1):                #inner loop handle the number of columns
#         print(i,end="")

#     print(" ")


# alphabet pyramid using for loop

# rows=int(input("Enter the number of rows"))
# ascii_value=65

# for i in range(rows):
#     for j in range(i+1):
#         alphabet=chr(ascii_value)
#         print(alphabet,end="")

#     ascii_value+=1
#     print()

# # Output :-
# Enter the number of rows5
# A
# BB
# CCC
# DDDD
# EEEEE


# Reverse pattern pyramid using python
# rows=int(input("Enter the number of rows        "))
# for i in range(rows+1,0,-1):
#     for j in range(0,i-1):
#         print("*",end="")

#     print()

# Enter the number of rows        5
# *****
# ****
# ***
# **
# *
      

# REVERSE NUMBER PYRAMID USING F0R LOOP
rows=int(input("Enter the number of rows"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print(i,end="")

    print()

# Enter the number of rows5
# 55555
# 4444
# 333
# 22
# 1