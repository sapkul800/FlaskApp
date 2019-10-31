# content of test_checkconfig.py
import pytest
import calculation

def checkconfig(x):
    __tracebackhide__ = True
    if not hasattr(x, "config"):
        pytest.fail("not configured: {}".format(x))


def test_add():
    assert(calculation.add(5,7), 12)

def test_mul():
    assert(calculation.mul(5,7), 35)
def test_sub():
    assert(calculation.sub(5,7), -2)
def test_div():
    assert(calculation.division(50,5), 10)
def test_div_err():
    assert(calculation.division(50,0), 0)