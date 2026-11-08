# Using function as an Argument
def func(text=""):
    return text.upper()


print(func("hello"))
yell = func
print(yell("hello again"))


# Using functions as an parameter in another function
def show(text):
    return text.lower()


def wrapper(func):
    greeting = func("I Called from ANOTHER function by passing arguments!")
    print(greeting)


wrapper(func)  # passing another function reference object
wrapper(show)


# Functions can return another function
def create_add(x):
    def add(y):
        return x + y

    return add


add_15 = create_add(15)
print(add_15(10))

# DECORATORS:modify the behaviour of function or class
print("Decorators:")

def hello_decorator(func):
    def inner1():
        print("Before calling of inner function")
        func()
        print("After calling the inner function")

    return inner1


def func_to_use():
    print("Im the function inside!")


hello_function = hello_decorator(func_to_use)
hello_function()


import math


def get_input(func):
    def inner():
        print("Before taking input")
        x = func()
        return x

    return inner


@get_input
def hello_input_fact():
    x = int(input("Enter a number:"))
    return math.factorial(x)


x = hello_input_fact()
print(x)


# Decor chaining


def decor1(func):
    def inner():
        x = func()
        return x * x  # 2*2=4   #27*27=729

    return inner


def decor2(func):
    def inner():
        x = func()
        return x * x * x  # 4*4*4=64 #3*3*3=27

    return inner


@decor1
@decor2
def hello_func():
    return 2


@decor2
@decor1
def hi_func():
    return 3


print(hello_func())
print(hi_func())