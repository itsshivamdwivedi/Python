#write a python program to find whether a given username contains less than 10 characters or not using if else statement
# username = input("Enter a username: ")

# if len(username) < 10:
#     print("Username contains less than 10 characters.")
# else:
#     print("Username contains 10 or more characters.")
# write a python program to find the greatest of four numbers using if else

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))

# greatest = num1

# if num2 > greatest:
#     greatest = num2

# if num3 > greatest:
#     greatest = num3

# if num4 > greatest:
#     greatest = num4

# print("The greatest number is:", greatest)



# efficient way to this same problem is showm below 
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))
# greatest = max(num1,num2,num3,num4)
# print("The greatest number is:", greatest)



# write a python program to find whether th given user  name is presnt in the list or not 
# def name_is_present(name,name_list):
#     if name in name_list:
#         return True
    
#     else:
#         return False
    
# names = ['shivam','vishal','harsh']
# search_name = input("Enter the name:")

#  if else practice examples  
# write a program to check whether the year is an leap year or not

# year = int(input("Enter your year"))
# if year %100 == 0:
#     if year %400 == 0:
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")
# else:
#     if year %4 == 0:
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# Write a program to accept the city name and display their monument

# city=input("Enter a city name")

# if city == "Mumbai":
#     print("The Monument in Mumbai is the Gateway of India")
# elif city == "Delhi":
#     print("The Monument in Delhi is the Taj Mahal")
# elif city == "Kolkata":
#     print("The Monument in Kolkata is the Shiv Sena Museum")
# else:
#     print("The given city is not acceptable")
       
# write a python program to take in the marks of 3 subjects and display in the grade

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "You are Failed"
    
marks =[]
for i in range(1,5):
    mark=int(input(f"Enter the marks of the subjects {i}:"))
    marks.append(mark)


# logic to calculate the average
average = sum(marks)/len(marks)
print(f"The average marks are: {average:.2f}")
print(f"Grade: {calculate_grade(average)}")


    
    
