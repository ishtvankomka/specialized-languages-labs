import pyfiglet


class TextArt:
    def __init__(self):
        self.text = ""
        self.font = ""
        self.width = ""

    def set_text(self, text):
        self.text = text

    def set_font(self, font):
        self.font = font

    def set_width(self, width):
        self.width = width

    def generate_text_art(self):
        figlet = pyfiglet.Figlet(font=self.font, width=self.width)
        generated_text_art = figlet.renderText(self.text)
        return generated_text_art
