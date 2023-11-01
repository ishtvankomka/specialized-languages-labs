from figures.figure import Figure
from helpers.helpers import paint_text


class Cube(Figure):
    def __init__(self):
        super().__init__()

    def generate_cube(self):
        n = self.size
        line = ''
        if n > 1:
            line += n * 2 * '_'
        else:
            line += '_'

        top_line = n * ' ' + line
        mid_line_space = 2 * n - 2
        mid_line = '/' + line + '/' + mid_line_space * ' ' + '\\'
        bottom_line = (n - 1) * ' ' + '\\' + line + '\/'

        inner_spaces = n * 2 * ' '
        inner_top = '/' + inner_spaces + '/'
        inner_bottom = '\\' + inner_spaces + '\\'

        top_content = ''
        bottom_content = ''

        for i in range(1, n):
            top_content += (n - i) * ' ' + inner_top + \
                (i - 1) * 2 * ' ' + '\\' + '\n'
            bottom_content += (i - 1) * ' ' + inner_bottom + \
                (n - i) * 2 * ' ' + '/' + '\n'

        cube = top_line + '\n' + top_content + mid_line + \
            '\n' + bottom_content + bottom_line + '\n'
        return cube

    def generate_figure(self):
        generated = self.generate_cube()
        colored = paint_text(generated, self.color)
        return colored
