class employee:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def empr(self):
        print(self.eid,self.ename,self.sal)
obj=employee(101,"Raveendra",1200000)
obj.empr()
