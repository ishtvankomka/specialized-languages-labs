from abc import ABC, abstractmethod
from figures.figure import Figure
from figures.figures_3d.cube import Cube
from figures.figures_2d.square import Square
from helpers.helpers import text_file_saver


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Generate3DFigureCommand(Command):
    def __init__(self, figure_interface):
        self.figure_interface = figure_interface

    def execute(self):
        print(self.figure_interface.generate_3d_figure())


class SetSizeCommand(Command):
    def __init__(self, figure_interface, new_size):
        self.figure_interface = figure_interface
        self.new_size = new_size

    def execute(self):
        self.figure_interface.set_size(self.new_size)


class SetColorCommand(Command):
    def __init__(self, figure_interface, new_color):
        self.figure_interface = figure_interface
        self.new_color = new_color

    def execute(self):
        self.figure_interface.set_color(self.new_color)


# Add more command classes for SetType, SetPaddings, Generate2DFigure, SaveToFile3D, and SaveToFile2D


class FigureArtInterface(Figure):
    def __init__(self):
        super().__init__()
        self.type = "cube"
        self.left_padding = 5
        self.top_padding = 5
        self.bottom_padding = 5
        self.commands = {
            1: Generate3DFigureCommand(self),
            2: SetSizeCommand(self, 0),
            3: SetColorCommand(self, ""),
            # Add more command instances here
        }

    def set_type(self, type):
        self.type = type

    def set_paddings(self, left_padding, top_padding, bottom_padding):
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.bottom_padding = bottom_padding

    def set_primary_data(self):
        size = int(input("figure size: "))
        self.set_size(size)

        color = input(
            "figure color(blue, green, red, magenta, yellow, white, cyan): ")
        self.set_color(color)

        type = input("figure type(skip for default): ")
        if len(type):
            self.set_type(type)

    def generate_with_left_padding(self, text):
        lines = text.split('\n')
        padded_lines = [f"{' ' * self.left_padding}{line}" for line in lines]
        return '\n'.join(padded_lines)

    def generate_with_top_padding(self, text):
        space = self.top_padding * '\n'
        padded_lines = space + text
        return padded_lines

    def generate_with_bottom_padding(self, text):
        space = self.bottom_padding * '\n'
        padded_lines = text + space
        return padded_lines

    def generate_with_paddings(self, text):
        return self.generate_with_bottom_padding(self.generate_with_top_padding(self.generate_with_left_padding(text)))

    def generate_3d_figure(self):
        if self.type == 'cube':
            cube = Cube()
            cube.set_size(self.size)
            cube.set_color(self.color)
            return self.generate_with_paddings(cube.generate_figure())
        return super().generate_figure()

    def generate_2d_figure(self):
        if self.type == 'cube':
            square = Square()
            square.set_size(self.size)
            square.set_color(self.color)
            return self.generate_with_paddings(square.generate_figure())
        return super().generate_figure()

    def save_to_file_2d(self):
        filename = input("enter filename before saving: ")
        text_file_saver(
            filename, self.generate_2d_figure())

    def save_to_file_3d(self):
        filename = input("enter filename before saving: ")
        text_file_saver(
            filename, self.generate_3d_figure())

    @staticmethod
    def show_menu():
        print("choose menu option")
        print("[ 1 ] - generate 3d figure")
        print("[ 2 ] - set size")
        print("[ 3 ] - set color(blue, green, red, magenta, yellow, white, cyan)")
        print("[ 4 ] - set type(cube)")
        print("[ 5 ] - set paddings")
        print("[ 6 ] - get 2d version of the figure")
        print("[ 7 ] - save to file(3d)")
        print("[ 8 ] - save to file(2d)")
        print("[ 0 ] - exit")

    def loop_menu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("menu key: "))
            if (menu_choice == 1):
                print(self.generate_3d_figure())
            elif (menu_choice == 2):
                new_size = int(input("enter new size: "))
                self.set_size(new_size)
            elif (menu_choice == 3):
                new_color = input("enter new color: ")
                self.set_color(new_color)
            elif (menu_choice == 4):
                new_type = input("enter new type: ")
                self.set_type(new_type)
            elif (menu_choice == 5):
                left_padding = int(input("enter left padding: "))
                top_padding = int(input("enter top padding: "))
                bottom_padding = int(input("enter bottom padding: "))
                self.set_paddings(left_padding, top_padding, bottom_padding)
            elif (menu_choice == 6):
                print(self.generate_2d_figure())
            elif (menu_choice == 7):
                self.save_to_file_3d()
            elif (menu_choice == 8):
                self.save_to_file_2d()
            else:
                break

    def launch(self):
        self.set_primary_data()
        print(self.generate_3d_figure())
        self.loop_menu()
