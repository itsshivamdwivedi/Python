# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the company name is {self.company}")
#     @classmethod
#     def changecompanyname(cls,NEWcompany):
#         cls.company = NEWcompany
# e1=Employee()
# e1.name = "harry"
# e1.changecompanyname("tesla")
# e1.show()
# print(Employee.company)

class Mathematics:
    def sum(self):
        print(20 + 30)

    def multiplication(self):
        rows = int(input("Enter the Number of Rows: "))
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print("*", end="")  # Print star on the same line
            print()  # Print new line after each row

sumvalue = Mathematics()
sumvalue.sum()  # Call sum method to print 20 + 30
sumvalue.multiplication()  # Call multiplication method

