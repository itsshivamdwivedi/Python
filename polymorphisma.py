class Ws:
    def Displayinfo(self):
        print("Hello World")
class Ms(Ws):
    def Displayinfo(self): 
        super().Displayinfo()  #super is used to call the parent function when two functions have same name
        print("jfnedjnci")
obj=Ms()
obj.Displayinfo()