from command.i_command import ICommand


class Generate3DFigureCommand(ICommand):
    def __init__(self, figure_interface):
        self.figure_interface = figure_interface

    def execute(self):
        print(self.figure_interface.generate_3d_figure())


class SetSizeCommand(ICommand):
    def __init__(self, figure_interface, new_size):
        self.figure_interface = figure_interface
        self.new_size = new_size

    def execute(self):
        self.figure_interface.set_size(self.new_size)
