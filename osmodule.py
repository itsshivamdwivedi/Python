# This code shows how to make many folder in just a seconds
import os
if(not os.path.exists("data")):
os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")


