import ast
import pytest
@pytest.fixture
def read_file():
    a=open("Text.txt","r")
    b=a.readline()
    print(b)
    c=b.split("=")[1].strip()
    d= b.split("=")[0].strip()
    print(c)
    out=ast.literal_eval(c)
    yield out
    a.close()



