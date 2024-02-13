#py.test -v -s -its for execute the all test_fiels
#py.test test_demo2.py -v -s -its for specific file run
#py.test -k creditcard -v -s -its for specific method run
#import pytest
#@pytest.mark.smoke -its for grouping the methods into smoke or sanity
#@pytest.mark.skip - its for skip the method
#@pytest.mark.xfail - its for run method but not show the results to console

import pytest
@pytest.mark.skip
def test_two():
    print("one")

@pytest.mark.xfail
def test_three():
    print("two")