from classes.command.i_command import ICommand


class DisplayBarchart(ICommand):
    def __init__(self, _app_receiver, data_frame):
        self._app_receiver = _app_receiver
        self.data_frame = data_frame

    def execute(self):
        self._app_receiver.run_display_barchart(self.data_frame)


class DisplayPiechart(ICommand):
    def __init__(self, _app_receiver, data_frame):
        self._app_receiver = _app_receiver
        self.data_frame = data_frame

    def execute(self):
        self._app_receiver.run_display_piechart(self.data_frame)


class DisplayLinechart(ICommand):
    def __init__(self, _app_receiver, data_frame):
        self._app_receiver = _app_receiver
        self.data_frame = data_frame

    def execute(self):
        self._app_receiver.run_display_linechart(self.data_frame)


class DisplayAllcharts(ICommand):
    def __init__(self, _app_receiver, data_frame):
        self._app_receiver = _app_receiver
        self.data_frame = data_frame

    def execute(self):
        self._app_receiver.run_display_allcharts(self.data_frame)


class SaveChartCommand(ICommand):
    def __init__(self, _app_receiver, data_frame, filename):
        self._app_receiver = _app_receiver
        self.data_frame = data_frame
        self.filename = filename

    def execute(self):
        self._app_receiver.run_save_chart(self.data_frame, self.filename)
