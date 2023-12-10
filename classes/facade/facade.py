
from classes.calculator_app.calculator_app import CalculatorApp
from classes.csv_display_app.csv_display_app import CsvDisplayApp
from classes.custom_text_art_app.custon_text_art_app import CustomTextArtApp
from classes.figure_art_app.figure_art_app import FigureArtApp
from classes.web_service_app.web_service_app import WebServiceApp


class Facade:
    def __init__(self):
        self.calculator = CalculatorApp()
        self.custom_text_art = CustomTextArtApp()
        self.figure_art = FigureArtApp()
        self.web_service = WebServiceApp()
        self.csv_display = CsvDisplayApp()

    def run_calculator(self):
        self.calculator.run()

    def run_custom_text_art(self):
        self.custom_text_art.run()

    def run_figure_art(self):
        self.figure_art.run()

    def run_web_service(self):
        self.web_service.run()

    def run_csv_display(self):
        self.csv_display.run()
