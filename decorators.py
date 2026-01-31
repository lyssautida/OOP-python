from typing import Any

def my_decorator(func):
    def wrapper():
        print("Before caling function")
        func()
        print("After calling function")
    return wrapper
    
@my_decorator
def my_function():
    print("My function has been called")

my_function()


class MyClassDecorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Before calling function (class decorator)")
        self.func()
        print("After calling function (class decorator)")

@MyClassDecorator
def second_function():
    print("Second function has been called")


second_function()

