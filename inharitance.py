class base:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def showdata(self):
        print("id:",self.id,"name:",self.name)

class derived(base):
    def hello(self):
        print("Hello Dear")

a=derived(1,"bhautik")
a.hello()
a.showdata()
