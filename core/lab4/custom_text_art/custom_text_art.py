from custom_text_art.helpers.helpers import paint_text, replace_symbol
from custom_text_art.text_art.text_art import TextArt


class CustomTextArt(TextArt):
    def __init__(self):
        super().__init__()
        self.symbol_to_replace = ""
        self.color = ""

    def set_symbol_to_replace(self, symbol_to_replace):
        self.symbol_to_replace = symbol_to_replace

    def set_color(self, color):
        self.color = color

    def generate_custom_text_art(self):
        generated_text_art = self.generate_text_art()
        custom_text_art_replaced = replace_symbol(
            generated_text_art, self.symbol_to_replace)
        custom_text_art_painted = paint_text(
            custom_text_art_replaced, self.color)
        return custom_text_art_painted
