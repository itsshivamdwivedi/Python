# s = "my name is shivam"
# with open("test.txt","w") as f :
#     f.write(s)
# fp = open("test.txt","w")
# fp.write(s)
# fp.close()
# s = "my name is shivam"
# with open("test.txt","w") as f :
#     f.write(s)
# fp = open("test.txt","w")
# fp.write(s)
# fp.close()

# how to read a file in python 
# with open("xyz.txt","r") as f:
#  s = f.read()
# print(s)
# f = open("xyz.txt","r")
# s= f.read()
# f.close()
# print(s)
# with open("test.txt","a") as f:
#     f.write("shivam is a bad boy who loves to code ")
# to read a file in python we use the readlines method 
f = open("xyz.txt", "r")
i =0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of the student {i} in maths is{m1}")
    print(f"Marks of the student {i} in english is{m2}")
    print(f"Marks of the student {i} in hindi is{m3}")