import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError("Can't square root a negative number!")
    return math.sqrt(x)


def modulus(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return x % y
