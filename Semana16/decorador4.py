registry = set()

def register(active=True):
    def decorate(func):
        print('executando registro(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('executando f1()')


@register()
def f2():
    print('executando f2()')


def f3():
    print('executando f3()')
