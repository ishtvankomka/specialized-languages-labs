from custom_text_art_interface.custon_text_art_interface import CustomTextArtInterface
import pyfiglet
from termcolor import colored
import re


def main():
    """ text = input("your text: ")
    font_name = input("art font: ")
    symbol_to_replace = input("art symbol(skip for default font symbols): ")
    color = input("art color: ")
    art_width = int(input("art width: "))

    figlet = pyfiglet.Figlet(font=font_name, width=art_width)

    ascii_art_text = figlet.renderText(text)

    pattern = r'\S'
    replaced_ascii_art_text = re.sub(pattern, symbol_to_replace, ascii_art_text)
    colored_art_text =  colored(replaced_ascii_art_text, color)

    print("your art:\n")
    print(ascii_art_text)
    print(replaced_ascii_art_text)
    print(colored_art_text) """
    
    custon_text_art_interface = CustomTextArtInterface()
    custon_text_art_interface.launch()


if __name__ == '__main__':
    main()
