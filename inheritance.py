# inheritance in python
class A:
    def DisplayA(self):
        print("HEllo Guys")
class B(A):
    def DisplayB(self):
        print("I am B")
class C(B):
    def DisplayC(self):
        print("I am C")
obj=C()
obj.DisplayC()
obj=B()
obj.DisplayA()
obj.DisplayB()