"""
A small GUI app to display a decimal clock
"""
from src.ui.main_window import MainWindow


APP_NAME = 'Decimal Clock'
APP_VERSION = '1.1'
SHIFT_START = '6:40:00'
SHIFT_LEN = 8


class App:
    def __init__(self):
        self.main_window = MainWindow(
            app_name=APP_NAME,
            app_version=APP_VERSION,
            shift_start=SHIFT_START,
            shift_len=SHIFT_LEN
        )

    def run(self):
        self.main_window.run()


if __name__ == '__main__':
    app = App()
    app.run()
