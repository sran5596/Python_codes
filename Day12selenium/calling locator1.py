from Day12selenium.Locators1 import d1
class child(d1):
    pass
    num1=12
    def __init__(self):
        d1.__init__(self,5,6)
    def mul(self):
        return self.num * self.num1
obj=child()
obj.p1()
print(obj.mul())
