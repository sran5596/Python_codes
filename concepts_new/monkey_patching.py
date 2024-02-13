#monkey patching
class Test:
    def one(self):
        print("one")
def two():
    print("two")
Test.one(1) # its print the function print="one"
Test.one=two # class.method=monkey function [print="two"]
Test.one()

