import math


class Operation:
    def execute(self):
        pass


class InputValidator:
    def __init__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("Invalid number format for input")


class Addition(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 + self.num2


class Subtraction(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 - self.num2


class Multiplication(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 * self.num2


class Division(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.num1 / self.num2


class Power(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 ** self.num2


class SquareRoot(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        self.num1 = num1

    def execute(self):
        if self.num1 < 0:
            raise ValueError(
                "Square root of a negative number is not possible.")
        return math.sqrt(self.num1)


class Modulo(Operation):
    def __init__(self, num1, num2):
        InputValidator(num1)
        InputValidator(num2)
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 % self.num2
