a=[1,2,3,4,5]
def number_check(a):
    for i in a:
        if i==2:
            #return True
            print("Yes")
            break
number_check(a)


a=[1,2,3,4,5]
def num_check(a):
    if 21 in a:
        print("Yes")
    elif 21 not in a:
        print("No")
    else:
        print("Try Next time")
num_check(a)

#Switch case:
a=[1,2,3,4,5,6,7]
def check(a):
    n="Hello"
    match n:
        case 1:
            print("Hema")
        case "Hello":
            print("Hi")
check(a)


check(a)
point = (0, 1)
match point:
    case (0, 0):
        print("Origin")
    case (x, y):
        print(x,y)



