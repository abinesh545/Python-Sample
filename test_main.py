from main import addition,subtraction
def test_add():
    assert addition(2,3)==5
    assert addition(7,0)==7
def test_sub():
    assert subtraction(5,4)==1
    assert subtraction(-7,-9)==2
    assert subtraction(-6,98)==-104
