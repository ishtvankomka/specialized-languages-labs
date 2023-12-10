class CalculatorError:
    def __init__(self, error_type, message):
        self.error_type = error_type
        self.message = message

    def __str__(self):
        return f'{self.error_type}: {self.message}'


def handle_error(exception):
    return CalculatorError(type(exception), exception.__str__())
