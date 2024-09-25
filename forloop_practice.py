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

