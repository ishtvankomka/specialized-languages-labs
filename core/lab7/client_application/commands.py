from command.i_command import ICommand


class GetApiDataCommand(ICommand):
    def __init__(self, _app_receiver, route, size, history, display_type, color):
        self._app_receiver = _app_receiver
        self.route = route
        self.size = size
        self.history = history
        self.display_type = display_type
        self.color = color

    def execute(self):
        self._app_receiver.run_get_api_data(
            self.route, self.size, self.history, self.display_type, self.color)


class GetHistoryDataCommand(ICommand):
    def __init__(self, _app_receiver, history, display_type, color):
        self._app_receiver = _app_receiver
        self.history = history
        self.display_type = display_type
        self.color = color

    def execute(self):
        self._app_receiver.run_get_history_data(
            self.history, self.display_type, self.color)


class SaveDataToTxtFileCommand(ICommand):
    def __init__(self, _app_receiver, history, display_type, filename):
        self._app_receiver = _app_receiver
        self.history = history
        self.display_type = display_type
        self.filename = filename

    def execute(self):
        self._app_receiver.run_save_data_to_txt_file(
            self.history, self.display_type, self.filename)


class SaveDataToJsonFileCommand(ICommand):
    def __init__(self, _app_receiver, history, display_type, filename):
        self._app_receiver = _app_receiver
        self.history = history
        self.display_type = display_type
        self.filename = filename

    def execute(self):
        self._app_receiver.run_save_data_to_json_file(
            self.history, self.display_type, self.filename)
