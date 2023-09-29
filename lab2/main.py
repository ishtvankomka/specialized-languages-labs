class Calculator:
    def __init__(self):
        self.result = 0.0
        self.choice = ''
        self.num1 = 0.0
        self.num2 = 0.0

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice

    def set_num1(self, num1):
        self.num1 = num1

    def set_num2(self, num2):
        self.num2 = num2

    def get_result(self):
        return self.result

    def add(self):
        self.result = self.num1 + self.num2

    def subtract(self):
        self.result = self.num1 - self.num2

    def multiply(self):
        self.result = self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError('Division by zero is not allowed')
        self.result = self.num1 / self.num2

    def power(self):
        self.result = self.num1 ** self.num2

    def square_root(self):
        if self.num1 < 0:
            raise ValueError('Square root of a negative number is not allowed')
        self.result = self.num1 ** 0.5

    def modulo(self):
        if self.num2 == 0:
            raise ValueError('Division by zero is not allowed')
        self.result = self.num1 % self.num2

    @staticmethod
    def get_number_input(prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    @staticmethod
    def get_user_choice():
        return input('Operation: [ +, -, *, /, ^, √, % ]: ')

    def get_input_choice(self):
        while True:
            choice = self.get_user_choice()
            if choice in ('+', '-', '*', '/', '^', '√', '%'):
                self.set_choice(choice)
                break
            else:
                print('Invalid choice. Please try again.')

    def get_input_num1(self):
        while True:
            try:
                num1 = float(input('Enter the first number: '))
                self.set_num1(num1)
                break
            except ValueError:
                print('Please enter a valid number.')

    def get_input_num2(self):
        if self.choice != '√':
            while True:
                try:
                    num2 = float(input('Enter the second number: '))
                    self.set_num2(num2)
                    break
                except ValueError:
                    print('Please enter a valid number.')

    def get_input_data(self):
        self.get_input_choice()
        self.get_input_num1()
        self.get_input_num2()

    def handle_input_data(self):
        try:
            if self.choice == '+':
                self.add()
            elif self.choice == '-':
                self.subtract()
            elif self.choice == '*':
                self.multiply()
            elif self.choice == '/':
                self.divide()
            elif self.choice == '^':
                self.power()
            elif self.choice == '√':
                self.square_root()
            elif self.choice == '%':
                self.modulo()
        except ValueError as e:
            print(e)

    @staticmethod
    def ask_user_to_continue():
        result = input('Do you want to continue? (y/n) ')
        return result == 'y'

    def user_interface(self):
        while True:
            try:
                self.get_input_data()
                self.handle_input_data()
                print(f'Result: {self.get_result()}')
            except:
                print('Something went wrong. Please try again.')

            to_continue = self.ask_user_to_continue()
            if to_continue == 0:
                print('change da world\nmy final message. Goodb ye')
                break


def main():
    calc = Calculator()
    calc.user_interface()


if __name__ == '__main__':
    main()
