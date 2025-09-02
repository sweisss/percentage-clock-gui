"""
A small GUI app to display a decimal clock
"""
import tkinter as tk
from tkinter import ttk

from src.ui.main_frame import MainFrame


APP_NAME = 'Decimal Clock'
APP_VERSION = '0.1'
# ICON_FILE = ...
STARTING_WINDOW_WIDTH = 600
STARTING_WINDOW_HEIGHT = 100


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.title(f'{APP_NAME} v{APP_VERSION}')
        # self.iconbitmap(self, ICON_FILE)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.window_width = STARTING_WINDOW_WIDTH
        self.window_height = STARTING_WINDOW_HEIGHT
        self.set_window_geometry()

        self.main_window = MainFrame()

    def set_window_geometry(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = self.window_width
        height = self.window_height
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def run(self):
        self.main_window.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
