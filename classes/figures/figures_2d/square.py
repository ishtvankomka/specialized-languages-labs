from classes.figures.figure import Figure
from helpers.helpers import paint_text


class Square(Figure):
    def __init__(self):
        super().__init__()

    def generate_square(self):
        n = self.size
        line = ''
        if n > 1:
            line += n * 2 * '_'
        else:
            line += '_'

        top_line = ' ' + line
        bottom_line = '|' + line + '|' + '\n'

        inner_spaces = n * 2 * ' '
        inner_fill = '|' + inner_spaces + '|'
        content = ''

        i = 1
        while (i < n):
            content += inner_fill + '\n'
            i += 1

        square = top_line + '\n' + content + bottom_line
        return square

    def generate_figure(self):
        generated = self.generate_square()
        colored = paint_text(generated, self.color)
        return colored
