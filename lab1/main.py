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

def main():
    history = []  # history of calculations
    memory = None  
    decimal_places = 2  # decimal places

    while True:
        try:
            print("Main Menu:")
            print("1. Calculations")
            print("2. Other")
            print("3. Exit")
            choice = input("Choose an option (1/2/3): ")

            if choice == '1':
                while True:
                    try:
                        num1 = float(input("First number: "))
                        num2 = float(input("Second number: "))
                        
                        operator = input("Choose operation (+, -, *, /, ^, √, %): ")
                        if operator in ('+', '-', '*', '/', '^', '√', '%'):
                            if operator == '+':
                                result = add(num1, num2)
                            elif operator == '-':
                                result = subtract(num1, num2)
                            elif operator == '*':
                                result = multiply(num1, num2)
                            elif operator == '/':
                                result = divide(num1, num2)
                            elif operator == '^':
                                result = power(num1, num2)
                            elif operator == '√':
                                result = square_root(num1)
                            elif operator == '%':
                                result = modulus(num1, num2)

                            # save calculation in history
                            expression = f"{num1} {operator} {num2} = {result}"
                            history.append(expression)

                            print(f"Result: {result:.{decimal_places}f}")

                            # Ask if the user wants to continue
                            again = input("Want to continue? (y/n): ")
                            if again.lower() != 'y':
                                break
                        else:
                            print("Incorrect operation!")

                    except ValueError:
                        print("Error: input data is not a number!")
                    except Exception as e:
                        print(f"Error: {e}")

            elif choice == '2':
                while True:
                    print("Other Menu:")
                    print("1. Memory (M)")
                    print("2. Recall Memory (R)")
                    print("3. History (H)")
                    print("4. Set Decimal Places (S)")
                    print("5. Decimalize Result (D)")
                    print("6. Back to Main Menu")
                    other_choice = input("Choose an option (1/2/3/4/5/6): ")
                    
                    if other_choice == '1':
                        memory = result
                        print("Result saved in memory.")
                    elif other_choice == '2':
                        if memory is not None:
                            print(f"Memory value: {memory:.{decimal_places}f}")
                        else:
                            print("Memory is empty")
                    elif other_choice == '3':
                        print("History of calculations:")
                        for entry in history:
                            print(entry)
                    elif other_choice == '4':
                        decimal_places = int(input("Set decimal places: "))
                    elif other_choice == '5':
                        result = round(result, decimal_places)
                        print(f"Result: {result:.{decimal_places}f}")
                    elif other_choice == '6':
                        break
                    else:
                        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")

            elif choice == '3':
                print("Goodbye!")
                return

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
