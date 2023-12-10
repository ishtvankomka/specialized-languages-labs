class MathOperationError(Exception):
    """
    error which throwed during mathematical operation
    """
    pass


class MathOperation:
    """
    basic math operation class for two numbers
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        pass

    def error_handler(self, error_text):
        raise MathOperationError(error_text)
