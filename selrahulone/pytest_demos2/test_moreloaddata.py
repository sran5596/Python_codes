import pytest

@pytest.mark.usefixtures("moredata")
@pytest.mark.usefixtures("moredata2")
class datadriven:
    def test_moredataload(self,moredata):
        print(moredata[0])

    def test_moredataload2(self,moredata2):
        print(moredata2[0])

#py.test -v -s = All
#py.test test_fixturedemo1.py -v -s  =specific file
#py.test -k credit -v -s = specific testmethod

#pytest.mark.smoke
#py.test -m smoke -v -s =sp[ecif marked methods as smoke or regression ..
#pytest.mark.skip = skips the test when ever you run
#pytest.mark.xfail = runs buit not show the result


