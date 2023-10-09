import re
from termcolor import colored


def replace_symbol(text, symbol_to_replace):
    if (len(symbol_to_replace)):
        pattern = r'\S'
        replaced = re.sub(pattern, symbol_to_replace, text)
        return replaced
    else:
        return text


def paint_text(text, color):
    if (len(color)):
        painted = colored(text, color)
        return painted
    else:
        return text
