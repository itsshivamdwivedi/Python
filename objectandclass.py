class person:
    name="harry"
    occupation='software developer'
    networth=10
    def info(self):
      print(f"{self.name} is a {self.occupation}")   
a = person()
b = person()
c = person()


a.name = "shubham"
a.occupation='teacher'

b.name="shivam"
b.occupation="chor"

c.name="bewakoof"
c.occupation="yedagiri"

a.info()
b.info()
c.info()
