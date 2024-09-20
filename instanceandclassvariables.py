# instance and class variable in python
class Employee:
    companyname="apple" #this is the example of the class variables
    noOfemployee=0
    def __init__(self,name):
        self.name=name
        self.raiseamount=0.02 # this is the example of the instance variables 
        Employee.noOfemployee += 1
    def showdetails(self):
        print(f"The name of the employee in {self.companyname} is {self.name} is the {self.noOfemployee}in company")
    
emp1 = Employee("harry")
emp2 = Employee("shivam")
emp1.raiseamount = 0.5 # we can change it thus it is an instance variables
emp1.companyname = "apple india"
emp2.companyname = "birla"
emp2.showdetails()
emp1.showdetails()