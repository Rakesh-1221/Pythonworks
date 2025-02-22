def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator                   #it equavalent to say_hello=decorator(say_hello)
def say_hello():
    print("Hello!")
say_hello()
