#  write a program in python that takes a list of strings and creates a new string that contains the lengths of each string

words=["hello","Shivam","How","redmi"]
lengths=[]
for word in words:
    lengths.append(len(word))
print(lengths)