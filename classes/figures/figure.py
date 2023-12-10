class Figure:
    """
    basic geometric figure class
    """
    def __init__(self):
        self.size = 1
        self.color = 'green'

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def generate_figure(self):
        return ""
