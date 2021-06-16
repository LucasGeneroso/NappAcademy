def f1(a):
    print(a)
    print(b)

b = 10
f1(15)

def f2(a):
    print(a)
    print(b)
    b = 9

# f2(10)

def f3(a):
    global b
    print(a)
    print(b)
    b = 10

f3(20)
print(b)

from dis import dis
dis(f1)
dis(f2)
