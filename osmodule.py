# This code shows how to make many folder in just a seconds
# import os
# try:
#      if(not os.path.exists("data")):
#        os.mkdir("data")

#      for i in range(0,100):
#          os.mkdir(f"data/Day{i+1}")
# except Exception as e:
#       print(f"An error occurred: {e}")
#       print("We are going to learn the os module in detail")


# In the above code i have used the try except exception to run the code of next line even if the error 
# occured in the previous line

# We  use mkdir() to make the new directory
# We use the path.exists method to check whether the path exists or not 

# import os
# try:
#      if(not os.path.exists("data")):
#        os.mkdir("data")

#      for i in range(0,100):
#          old_name=f"data/Day{i+1}"
#          new_name=f"data/Python{i+1}"
#          os.rename(old_name,new_name)         #this is how we can change the names of the files in the directories 
# except Exception as e:
#       print(f"An error occurred: {e}")
#       print("We are going to learn the os module in detail")


