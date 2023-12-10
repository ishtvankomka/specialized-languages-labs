class Invoker:
    """invoker class for command pattern"""
    def __init__(self):
        self.commands = []
        self.current = 0

    def add_command(self, command):
        self.commands.append(command)

    def execute_command(self, index):
        self.commands[index].execute()
        self.current = index + 1

    def execute_current_command(self):
        self.commands[self.current].execute()
        self.current += 1

    def execute_last_command(self):
        self.commands[len(self.commands)-1].execute()
