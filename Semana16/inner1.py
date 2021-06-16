def outer_func():
    def inner_func():
        print("Hi, World!")
    inner_func()

outer_func()


def outer_func2(who):
    def inner_func():
        print(f"Hi, {who}!")
    inner_func() 

outer_func2('World')


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Desculpe. 'numbero' precisa ser inteiro.")
    if number < 0:
        raise ValueError("Desculpe. 'nuimero' precisa ser zero ou positivo.")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(5))