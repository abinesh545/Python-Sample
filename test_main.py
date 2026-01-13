from main import addition,subtraction,multiplication,division,modulo
import pytest
    assert addition(2,3)==5
    assert addition(7,0)==7
def test_sub():
    assert subtraction(5,4)==1
    assert subtraction(-7,-9)==2
    assert subtraction(-6,98)==-104
def test_mul():
    assert multiplication(3,4)==12
    assert multiplication(5,0)==0
    assert multiplication(1,10000)==10000
def test_div():
    assert division(54,9)==6
    assert division(72,4)==18
    with pytest.raises(ValueError, match="Cannot Divide by Zero"):
        division(32, 0)
def test_mod():
    assert modulo(45,4)==1
    assert modulo(23,1)==0
