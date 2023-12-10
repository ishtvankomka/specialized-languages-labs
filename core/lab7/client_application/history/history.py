class History:
    def __init__(self):
        self.history = []

    def log(self, data):
        self.history.append(data)

    def get_history(self):
        return self.history
