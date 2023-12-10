import math
from math_operations.math_operation import MathOperation


class Addition(MathOperation):
    def execute(self):
        return self.num1 + self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during addition: {error}")


class Subtraction(MathOperation):
    def execute(self):
        return self.num1 - self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during subtraction: {error}")


class Multiplication(MathOperation):
    def execute(self):
        return self.num1 * self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during multiplication: {error}")


class Division(MathOperation):
    def execute(self):
        if self.num2 == 0:
            self.error_handler('Division by zero is not allowed')
        return self.num1 / self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during division: {error}")


class Power(MathOperation):
    def execute(self):
        return self.num1 ** self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during exponentiation: {error}")


class SquareRoot(MathOperation):
    def execute(self):
        if self.num1 < 0:
            self.error_handler(
                'Square root of a negative number is not allowed')
        return math.sqrt(self.num1)

    def error_handler(self, error):
        raise ValueError(f"Error during square root: {error}")


class Modulo(MathOperation):
    def execute(self):
        if self.num2 == 0:
            self.error_handler('Division by zero is not allowed')
        return self.num1 % self.num2

    def error_handler(self, error):
        raise ValueError(f"Error during modulo operation: {error}")
