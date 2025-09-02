"""
The main tkinter window of the app.
"""
import tkinter as tk
from tkinter import ttk

from src.ui.main_frame import MainFrame


# ICON_FILE = ...
STARTING_WINDOW_WIDTH = 600
STARTING_WINDOW_HEIGHT = 175


class MainWindow(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__()

        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.title(f'{kwargs.get('app_name')} v{kwargs.get('app_version')}')
        # self.iconbitmap(self, ICON_FILE)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.window_width = STARTING_WINDOW_WIDTH
        self.window_height = STARTING_WINDOW_HEIGHT
        self.set_window_geometry()

        self.main_frame = MainFrame(master=self, shift_start=kwargs.get('shift_start'), shift_len=kwargs.get('shift_len'))

    def set_window_geometry(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = self.window_width
        height = self.window_height
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def run(self):
        self.main_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.mainloop()
