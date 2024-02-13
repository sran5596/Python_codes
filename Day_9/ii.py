from Day_9.modulespackegs import cal


class one(cal):
    num1=120
    def __init__(self):
        cal.__init__(self,3,4)

    def sum(self,r,y):
        self.r=r
        self.y=y
        print(self.num+self.num1)
obj=one()
obj.sum(3,4)