from Udemy.Practise import raveendra


class ravikumar(raveendra):
    num2=150

    def __int__(self):
        raveendra.__int__(self,3 , 5)

    def sumval1(self):
        return self.num+self.num2+self.sumval()


obj=ravikumar()
print(obj.__int__())
print(obj.sumval1())
