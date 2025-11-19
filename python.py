import ast
def read_file():
    a=open("Text.txt","r")
    b=a.readline()
    print(b)
    c=b.split("=")[1].strip()
    d= b.split("=")[0].strip()
    print(c)
    out=ast.literal_eval(c)
    print(out)
    yield out
    a.close()
read_file()





