def deco(func):
    def inner():
        print('Executando inner()')
    return inner

@deco
def target(): 
    print('Executando target()')

target() 
target