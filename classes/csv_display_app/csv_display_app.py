from classes.command.invoker import Invoker
from classes.csv_display_app.commands import DisplayAllcharts, DisplayBarchart, DisplayLinechart, DisplayPiechart, SaveChartCommand
from classes.csv_display_app.csv_display_app_receiver import CsvDisplayAppReceiver
import pandas as pd


class CsvDisplayApp():
    def __init__(self):
        self.data_source = 'data/data.csv'
        self.data_frame = None
        self.app_receiver = CsvDisplayAppReceiver()
        self.app_invoker = Invoker()

    def set_data_source(self, val):
        self.data_source = val

    def set_data_frame(self, val):
        self.data_frame = val

    def set_primary_data(self):
        data_source = input(
            "enter filename of datasource(skip for default): ")
        if len(data_source):
            self.set_data_source(data_source)
        self.set_data_frame(pd.read_csv(self.data_source))

    def display_barchart(self):
        display_barchart_command = DisplayBarchart(
            self.app_receiver, self.data_frame)
        self.app_invoker.add_command(display_barchart_command)
        self.app_invoker.execute_current_command()

    def display_piechart(self):
        display_piechart_command = DisplayPiechart(
            self.app_receiver, self.data_frame)
        self.app_invoker.add_command(display_piechart_command)
        self.app_invoker.execute_current_command()

    def display_linechart(self):
        display_linechart_command = DisplayLinechart(
            self.app_receiver, self.data_frame)
        self.app_invoker.add_command(display_linechart_command)
        self.app_invoker.execute_current_command()

    def display_allcharts(self):
        display_allcharts_command = DisplayAllcharts(
            self.app_receiver, self.data_frame)
        self.app_invoker.add_command(display_allcharts_command)
        self.app_invoker.execute_current_command()

    def save_chart(self, filename):
        save_chart_command = SaveChartCommand(
            self.app_receiver, self.data_frame, filename)
        self.app_invoker.add_command(save_chart_command)
        self.app_invoker.execute_current_command()

    @staticmethod
    def show_menu():
        print("choose menu option")
        print("[ 1 ] - display bar chart")
        print("[ 2 ] - display pie chart")
        print("[ 3 ] - display line chart")
        print("[ 4 ] - display all charts")
        print("[ 5 ] - change sourcefile")
        print("[ 6 ] - save chart")
        print("[ 0 ] - exit")

    def loop_menu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("menu key: "))

            if (menu_choice == 1):
                self.display_barchart()
            elif (menu_choice == 2):
                self.display_piechart()
            elif (menu_choice == 3):
                self.display_linechart()
            elif (menu_choice == 4):
                self.display_allcharts()
            elif (menu_choice == 5):
                new_sourcefile = input("enter filename of new datasource: ")
                if len(new_sourcefile):
                    self.set_data_source(new_sourcefile)
                self.set_data_frame(pd.read_csv(new_sourcefile))
            elif (menu_choice == 6):
                filename = input("enter filename: ")
                if len(filename):
                    self.save_chart(filename)
                else:
                    self.save_chart('chart.png')
            else:
                break

    def launch(self):
        self.set_primary_data()
        self.display_barchart()
        self.loop_menu()
        
    def run(self):
        self.launch()