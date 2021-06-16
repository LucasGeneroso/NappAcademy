registry = []
def register(func):
    print('Executando registro(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('executandof1()')

@register
def f2():
    print('executandof2()')

def f3():
    print('executandof3()')

def main():
    print('executando main()')
    print('Registrado ->', registry)
    f1()
    f2()
    f3()

main()
