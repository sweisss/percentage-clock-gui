"""
A small GUI app to display a decimal clock
"""
import sys
import platform

from src.ui.main_window import MainWindow


APP_NAME = 'Percentage Clock'
APP_VERSION = '2.4'
SHIFT_START = '6:40:00'
SHIFT_LEN = 10


class App:
    def __init__(self):
        pltfrm = platform.system()

        shift_start = sys.argv[1] if len(sys.argv) >= 2 else SHIFT_START
        shift_len = float(sys.argv[2]) if len(sys.argv) == 3 else SHIFT_LEN

        self.main_window = MainWindow(
            pltfrm=pltfrm,
            app_name=APP_NAME,
            app_version=APP_VERSION,
            shift_start=shift_start,
            shift_len=shift_len
        )

    def run(self):
        self.main_window.run()


if __name__ == '__main__':
    app = App()
    app.run()
