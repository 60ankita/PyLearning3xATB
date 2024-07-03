def decorator1(func):
    def wrapper():
        print("Decorator")
        func()
    return wrapper()

def decorator2(func):
    def wrapper():
        print("hi")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello")
