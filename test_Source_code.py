import pytest
from Source_code import add,divide,flo,length
def test_add():
    assert add(2,3)==5
    assert add(4,5)!=10
    assert add(2,3)>3
    assert add(2,3)>=5
    assert add(5,6)<=11

def test_listed():
    a = [1, 2, "Apple", "Banana"]
    assert 1 in a
    assert 2 in a
    assert "Cherry" not in a
    assert "Apple" in a
    assert "Banana" in a

def test_string_check():
    a="Hello Hema World"
    assert a.startswith("Hello")
    assert a.endswith("World")

def test_divide():
    assert divide(5,2)==2.5

def test_divide_Error():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)

def test_flo():
    result=0.1+0.2
    assert result == pytest.approx(result)

def test_length():
    lst = [1,2,3,4]
    assert len(lst) == 4

def test_all_any():
    numbers = [2,4,6,8]
    assert all(n % 2 == 0 for n in numbers)   # all are even
    assert any(n > 5 for n in numbers)



