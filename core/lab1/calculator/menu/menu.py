def display_main_menu():
    print("Main Menu:")
    print("1. Calculations")
    print("2. Other")
    print("3. Exit")


def get_main_menu_choice():
    return input("Choose an option (1/2/3): ")


def display_other_menu():
    print("Other Menu:")
    print("1. Memory (M)")
    print("2. Recall Memory (R)")
    print("3. History (H)")
    print("4. Set Decimal Places (S)")
    print("5. Decimalize Result (D)")
    print("6. Back to Main Menu")


def get_other_menu_choice():
    return input("Choose an option (1/2/3/4/5/6): ")
