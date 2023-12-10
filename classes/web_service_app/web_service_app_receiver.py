from classes.command.receiver import Receiver
from helpers.helpers import api_data_to_type, api_data_to_type_painted, json_file_saver, text_file_saver
from classes.web_service.web_service import WebService


class WebServiceAppReceiver(Receiver):
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
