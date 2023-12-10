from calculator.menu.menu import display_main_menu, get_main_menu_choice, display_other_menu, get_other_menu_choice
from math_operations.math_operations import add, subtract, multiply, divide, power, square_root, modulus


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Input data is not a number!")


def get_operator_input():
    while True:
        operator = input("Choose operation (+, -, *, /, ^, √, %): ")
        if operator in ('+', '-', '*', '/', '^', '√', '%'):
            return operator
        else:
            print("Incorrect operation!")


def get_yes_or_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ('y', 'n'):
            return choice
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


def gather_input():
    num1 = get_float_input("First number: ")
    num2 = get_float_input("Second number: ")
    operator = get_operator_input()
    return num1, num2, operator


def calculate_result(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return power(num1, num2)
    elif operator == '√':
        return square_root(num1)
    elif operator == '%':
        return modulus(num1, num2)


def handle_memory(memory, result):
    memory = result
    print("Result saved in memory.")
    return memory


def handle_recall_memory(memory, decimal_places):
    if memory is not None:
        print(f"Memory value: {memory:.{decimal_places}f}")
    else:
        print("Memory is empty")


def handle_history(history):
    print("History of calculations:")
    for entry in history:
        print(entry)


def handle_set_decimal_places(decimal_places):
    new_decimal_places = int(input("Set decimal places: "))
    return new_decimal_places


def handle_decimalize_result(result, decimal_places):
    result = round(result, decimal_places)
    print(f"Result: {result:.{decimal_places}f}")
    return result


def handle_other_options(other_choice, memory, result, decimal_places, history):
    if other_choice == '1':
        memory = handle_memory(memory, result)
    elif other_choice == '2':
        handle_recall_memory(memory, decimal_places)
    elif other_choice == '3':
        handle_history(history)
    elif other_choice == '4':
        decimal_places = handle_set_decimal_places(decimal_places)
    elif other_choice == '5':
        result = handle_decimalize_result(result, decimal_places)
    elif other_choice == '6':
        return memory, decimal_places  # Return updated memory and decimal_places
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")

    return memory, result, decimal_places


def handle_main_calculation(num1, num2, operator, history, decimal_places):
    result = calculate_result(num1, num2, operator)
    # Save calculation in history
    expression = f"{num1} {operator} {num2} = {result}"
    history.append(expression)
    print(f"Result: {result:.{decimal_places}f}")
    return result


def handle_main_menu(choice, history, decimal_places):
    while choice == '1':
        try:
            num1, num2, operator = gather_input()
            result = handle_main_calculation(
                num1, num2, operator, history, decimal_places)

            # Ask if the user wants to continue
            again = get_yes_or_no_input("Want to continue? (y/n): ")
            if again == 'n':
                break
        except Exception as e:
            print(f"Error: {e}")


def handle_main_options(choice, history, decimal_places):
    if choice == '1':
        handle_main_menu(choice, history, decimal_places)
    elif choice == '2':
        while True:
            display_other_menu()
            other_choice = get_other_menu_choice()
            memory, result, decimal_places = handle_other_options(
                other_choice, memory, result, decimal_places, history
            )
    elif choice == '3':
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


def calculator():
    history = []  # history of calculations
    decimal_places = 2  # decimal places

    while True:
        try:
            display_main_menu()
            choice = get_main_menu_choice()

            handle_main_options(choice, history, decimal_places)

        except Exception as e:
            print(f"Error: {e}")
