import os
folders =os.listdir("data")    # list of the directories
print(folders)
# for folders in folders:
#     print(folders)


# To display the files of all the folder we can us a loop 
for folder in folders:
    print(os.listdir(f"/data/{folder}"))
    