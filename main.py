import logging
from classes.facade.facade import Facade


class App(Facade):
    def __init__(self):
        super().__init__()
        logging.basicConfig(filename='logs/example.log', level=logging.DEBUG)

    @staticmethod
    def log_info_run(run):
        """logs info of current running app"""
        logging.info('running ' + run)

    @staticmethod
    def log_error_run(run):
        """logs uncaugh error of current running app"""
        logging.error('uncaugh error in  ' + run)

    def show_menu(self):
        print("Choose an app to run:")
        print("1. calculator")
        print("2. custom text art")
        print("3. figure art")
        print("4. web service")
        print("5. csv display")
        print("0. Exit runner")

    def run_menu(self):
        while (True):
            self.show_menu()
            choice = input("Enter your choice (1/2/3/4/5/0): ")
            if choice == "1":
                self.log_info_run('calculator')
                try:
                    self.run_calculator()
                except:
                    self.log_error_run('calculator')
            elif choice == "2":
                self.log_info_run('custom text art')
                try:
                    self.run_custom_text_art()
                except:
                    self.log_error_run('custom text art')
            elif choice == "3":
                self.log_info_run('figure art')
                try:
                    self.run_figure_art()
                except:
                    self.log_error_run('figure art')
            elif choice == "4":
                self.log_info_run('web service')
                try:
                    self.run_web_service()
                except:
                    self.log_error_run('web service')
            elif choice == "5":
                self.log_info_run('csv display')
                try:
                    self.run_csv_display()
                except:
                    self.log_error_run('csv display')
            else:
                logging.debug('exit runner')
                print("Goodbye!")
                break


if __name__ == "__main__":
    app = App()
    app.run_menu()
