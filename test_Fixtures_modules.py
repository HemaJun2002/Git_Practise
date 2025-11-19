# test_class_scope.py
import pytest

@pytest.fixture(scope="class")
def class_data():
    print("\n[Setup] class_data")
    yield [1, 2, 3]
    print("\n[Teardown] class_data")

class TestExample:
    def test_sum(self, class_data):
        assert sum(class_data) == 6

    def test_len(self, class_data):
        assert len(class_data) == 3



