from classes.text_art.art_generator.art_generator import generate_custom_text


class TextArt:
    """
    basic class for text art generation
    """

    def __init__(self):
        self.text = ""
        self.font = ""

    def set_text(self, text):
        self.text = text

    def set_font(self, font):
        self.font = font

    def generate_text_art(self):
        return generate_custom_text(input_string=self.text, font_name=self.font)
