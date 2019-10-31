def add(a=0,b=0):
    return a+b

def mul(a=0,b=0):
    return a*b

def sub(a=0,b=0):
    return a-b

def division(a=0,b=0):
    c = 0
    try:
        c = a/float(b)
    except:
        pass
    return c
def sample_testcase():
    assert True == True                