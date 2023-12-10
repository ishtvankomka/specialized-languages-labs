from classes.custom_text_art.custom_text_art import CustomTextArt
from helpers.helpers import text_file_saver


class CustomTextArtApp:
    """
    class for app which uses custom text art class
    """
    def __init__(self):
        self.custom_text_art = CustomTextArt()

    def set_primary_data(self):
        text = input("your text: ")
        self.custom_text_art.set_text(text)
        font = input("art font: ")
        self.custom_text_art.set_font(font)

        symbol_to_replace = input(
            "art symbol(skip for default font symbols): ")
        self.custom_text_art.set_symbol_to_replace(symbol_to_replace)
        color = input("art color: ")
        self.custom_text_art.set_color(color)

    @staticmethod
    def show_menu():
        print("choose menu option")
        print("[ 1 ] - generate text art")
        print("[ 2 ] - set text")
        print("[ 3 ] - set font")
        print("[ 4 ] - set symbol")
        print("[ 5 ] - set color")
        print("[ 6 ] - save to file")
        print("[ 0 ] - exit")

    def save_to_file(self):
        filename = input("enter filename before saving: ")
        text_file_saver(
            filename, self.custom_text_art.generate_custom_text_art())

    def loop_menu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("menu key: "))
            if (menu_choice == 1):
                print(self.custom_text_art.generate_custom_text_art())
            elif (menu_choice == 2):
                new_text = input("enter new text: ")
                self.custom_text_art.set_text(new_text)
            elif (menu_choice == 3):
                new_font = input("enter new font: ")
                self.custom_text_art.set_font(new_font)
            elif (menu_choice == 4):
                new_symbol = input("enter new symbol: ")
                self.custom_text_art.set_symbol_to_replace(new_symbol)
            elif (menu_choice == 5):
                new_color = input("enter new color: ")
                self.custom_text_art.set_color(new_color)
            elif (menu_choice == 6):
                self.save_to_file()
            else:
                break

    def launch(self):
        self.set_primary_data()
        print(self.custom_text_art.generate_custom_text_art())
        self.loop_menu()

    def run(self):
        self.launch()
