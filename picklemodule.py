# in this we are going to learn about the pickle module in python

import pickle
# l=[20,20,20,20,20,20,20,20]
file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)
# pickle.dump(l,file)
# file.close()
# dump function is used to dump the content in the particular file
