#  write a program in python that takes a list of strings and creates a new string that contains the lengths of each string

words=["hello","Shivam","How","redmi"]
lengths=[]
for word in words:
    lengths.append(len(word))
print(lengths)


#  Write a program to print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

#  let's define the number of rows
rows=5
for i in range(1,rows + 1,1):

    for j in range(1,i+1):          #inner loop 
        print(j, end=" ")

    print(" ")


# WAP In python to calculate the sum of all numbers from 1 to a given number entered by the users

# number=int(input("Enter a number"))
# sum=0
# for i in range(1,number+1):
#     sum+=i
    
# print(f"Sum of all numbers from 1 to {number} is {sum}")

# Write a program to get the multiplication table of number given by the user

n=int(input("Enter a number of which you want multiplication table of"))

for i in range(1,11,1):
    product=n*i
    print(f"{n} x {i} = {product}")





