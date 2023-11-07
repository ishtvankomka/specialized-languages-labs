from calulator.operations.operations import Addition, Subtraction, Multiplication, Division, Power, SquareRoot, Modulo
from calulator.ui.error_handler.error_handler import handle_error


class Calculator:
    def __init__(self):
        self.result = 0.0

    def get_user_choice(self):
        return input('Operation: [ +, -, *, /, ^, √, % ]: ')

    def get_input_num(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print('Please enter a valid number.')

    def get_input_data(self):
        choice = self.get_user_choice()
        num1 = self.get_input_num('Enter the first number: ')
        num2 = None
        if choice not in ('√'):
            num2 = self.get_input_num('Enter the second number: ')
        return choice, num1, num2

    def perform_operation(self, choice, num1, num2):
        operation = None

        if choice == '+':
            operation = Addition(num1, num2)
        elif choice == '-':
            operation = Subtraction(num1, num2)
        elif choice == '*':
            operation = Multiplication(num1, num2)
        elif choice == '/':
            operation = Division(num1, num2)
        elif choice == '^':
            operation = Power(num1, num2)
        elif choice == '√':
            operation = SquareRoot(num1, None)
        elif choice == '%':
            operation = Modulo(num1, num2)

        if operation:
            try:
                self.result = operation.execute()
            except Exception as e:
                self.result = handle_error(e)
        else:
            self.result = handle_error(ValueError(
                'Invalid choice. Please try again.'))

    @staticmethod
    def ask_user_to_continue():
        result = input('Do you want to continue? (y/n) ')
        return result == 'y'

    def user_interface(self):
        while True:
            try:
                choice, num1, num2 = self.get_input_data()
                self.perform_operation(choice, num1, num2)
                print(f'Result: {self.result}')
            except Exception as e:
                print(f'Something went wrong: {e}. Please try again.')

            to_continue = self.ask_user_to_continue()
            if not to_continue:
                print('change da world\nmy final message. Goodb ye')
                break
