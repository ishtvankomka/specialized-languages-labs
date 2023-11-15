from command.receiver import Receiver
from command.i_command import ICommand
from command.invoker import Invoker
from client_application.history.history import History
from helpers.helpers import api_data_to_type, api_data_to_type_painted, json_file_saver, text_file_saver
from web_service.web_service import WebService


class ClientApplicationReceiver(Receiver):
    @staticmethod
    def run_get_api_data(route, size, history, display_type, color):
        ws = WebService(route, size)
        data = ws.get_data()
        history.log(data)
        print(api_data_to_type_painted(data, display_type, color))

    @staticmethod
    def run_get_history_data(history, display_type, color):
        history_log = history.get_history()
        result_log = ''
        for log in history_log:
            result_log += api_data_to_type_painted(log, display_type, color)
        print(result_log)

    @staticmethod
    def run_save_data_to_txt_file(history, display_type, filename):
        history_log = history.get_history()
        result_log = ''
        for log in history_log:
            result_log += api_data_to_type(log, display_type)
        text_file_saver(filename + '.txt', result_log)

    @staticmethod
    def run_save_data_to_json_file(history, display_type, filename):
        history_log = history.get_history()
        json_file_saver(filename + '.json', history_log)


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


class ClientApplication():
    def __init__(self):
        self.route = 'users'
        self.size = 5
        self.display_type = 'original'
        self.color = 'green'
        self.app_receiver = ClientApplicationReceiver()
        self.app_invoker = Invoker()
        self.history = History()

    def set_route(self, val):
        self.route = val

    def set_size(self, val):
        self.size = val

    def set_display_type(self, val):
        self.display_type = val

    def set_color(self, val):
        self.color = val

    def set_primary_data(self):
        route = input(
            "set route(users, addresses, banks, appliances, beers, blood_types, credit_cards): ")
        if len(route):
            self.set_route(route)

        size = int(input("set size: "))
        self.set_size(size)

        display_type = input(
            "set display type(original, list, table): ")
        if len(display_type):
            self.set_display_type(display_type)

        color = input(
            "set color(blue, green, red, magenta, yellow, white, cyan): ")
        if len(color):
            self.set_color(color)

    def get_api_data_for_current_config(self):
        get_api_data_command = GetApiDataCommand(
            self.app_receiver, self.route, self.size, self.history, self.display_type, self.color)
        self.app_invoker.add_command(get_api_data_command)
        self.app_invoker.execute_current_command()

    def get_history_data_for_current_config(self):
        get_history_data_command = GetHistoryDataCommand(
            self.app_receiver, self.history, self.display_type, self.color)
        self.app_invoker.add_command(get_history_data_command)
        self.app_invoker.execute_current_command()

    def save_to_txt_file(self):
        filename = input("enter filename before saving: ")
        save_data_to_txt_file_command = SaveDataToTxtFileCommand(
            self.app_receiver, self.history, self.display_type, filename)
        self.app_invoker.add_command(save_data_to_txt_file_command)
        self.app_invoker.execute_current_command()

    def save_to_json_file(self):
        filename = input("enter filename before saving: ")
        save_data_to_json_file_command = SaveDataToJsonFileCommand(
            self.app_receiver, self.history, self.display_type, filename)
        self.app_invoker.add_command(save_data_to_json_file_command)
        self.app_invoker.execute_current_command()

    @staticmethod
    def show_menu():
        print("choose menu option")
        print("[ 1 ] - get data")
        print("[ 2 ] - set route(users, addresses, banks, appliances, beers, blood_types, credit_cards)")
        print("[ 3 ] - set size")
        print("[ 4 ] - set display type(original, list, table)")
        print("[ 5 ] - set color(blue, green, red, magenta, yellow, white, cyan)")
        print("[ 6 ] - show history")
        print("[ 7 ] - save to txt")
        print("[ 8 ] - save to json")
        print("[ 0 ] - exit")

    def loop_menu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("menu key: "))

            if (menu_choice == 1):
                self.get_api_data_for_current_config()
            elif (menu_choice == 2):
                new_route = input("enter new route: ")
                self.set_route(new_route)
            elif (menu_choice == 3):
                new_size = int(input("enter new size: "))
                self.set_size(new_size)
            elif (menu_choice == 4):
                new_display_type = input("enter new display type: ")
                self.set_display_type(new_display_type)
            elif (menu_choice == 5):
                new_color = input("enter new color: ")
                self.set_color(new_color)
            elif (menu_choice == 6):
                self.get_history_data_for_current_config()
            elif (menu_choice == 7):
                self.save_to_txt_file()
            elif (menu_choice == 8):
                self.save_to_json_file()
            else:
                break

    def launch(self):
        self.set_primary_data()
        self.get_api_data_for_current_config()
        self.loop_menu()
