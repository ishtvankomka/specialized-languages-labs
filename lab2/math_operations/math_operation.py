class MathOperationError(Exception):
    pass


class MathOperation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        pass

    def error_handler(self, error_text):
        raise MathOperationError(error_text)
