try:
    a = int(input("Enter a number"))
    print(a+3)
except Exception as e:
    print("some error occured",e)
    # to knoow what error has occured in the program we can use the exception to know which type of error has been occured 