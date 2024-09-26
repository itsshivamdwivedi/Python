try:
    a = int(input("Enter a number"))
    print(a+3)
except Exception as e:
    print("some error occured",e)
    # to know what error has occured in the program we can use the exception to know which type of error has been occured 
    # we use the exception handling to keep executing the others lines of code
    # we can also use the error message to debug the code

    # Types of exceptions are syntax errors- occured due to invalid syntax.add
    # Type erros- occured due to invalid assigning of variable type
    #value error , Index error 