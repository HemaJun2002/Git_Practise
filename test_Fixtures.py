import pytest
@pytest.fixture
def simple_data():
    return [1,2,3,4,5]

def test_sum(simple_data):
    assert sum(simple_data)==15

def test_max(simple_data):
    assert max(simple_data)==5

def test_min(simple_data):
    assert min(simple_data)==1

