from figure_art_interface.figure_art_interface import FigureArtInterface

def main():
    
    figure_art_interface = FigureArtInterface()
    figure_art_interface.launch()
    
    """ def generate_cube(n=1):
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

        # return bottom_content

        cube = top_line + '\n' + top_content + mid_line + \
            '\n' + bottom_content + bottom_line + '\n'
        return cube

    print(generate_cube())
    print(generate_cube(2))
    print(generate_cube(4))
    print(generate_cube(5))

    def generate_square(n=1):
        line = ''
        if n > 1:
            line += n * 2 * '_'
        else:
            line += '_'

        top_line = ' ' + line
        bottom_line = '|' + line + '|'

        inner_spaces = n * 2 * ' '
        inner_fill = '|' + inner_spaces + '|'
        content = ''

        i = 1
        while (i < n):
            content += inner_fill + '\n'
            i += 1
            
        square = top_line + '\n' + content + bottom_line
        return square
    
    print(generate_square())
    print(generate_square(2))
    print(generate_square(4)) """
    

if __name__ == '__main__':
    main()
