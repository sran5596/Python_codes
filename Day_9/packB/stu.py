class student:
    def __init__(self,sid,sname,grad):
        self.sid=sid
        self.sname=sname
        self.grad=grad
    def stpr(self):
        print(self.sid,self.sname,self.grad)

obj=student(2,"samapthi",75)
obj.stpr()
