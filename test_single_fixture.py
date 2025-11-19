import pytest

@pytest.fixture(scope="module")        #Defaulty it will take scope = Function
def function():
    a=[1,2,3,4,5]
    return a

def test_sum(function):
    assert sum(function)==15

def test_max(function):
    assert max(function)==5

