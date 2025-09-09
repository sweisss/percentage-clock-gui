"""
The main tkinter window of the app.
"""
import tkinter as tk
from tkinter import ttk

from src.ui.main_frame import MainFrame
from src.ui.toolbar import Toolbar


# ICON_FILE = ...
STARTING_WINDOW_WIDTH = 550
STARTING_WINDOW_HEIGHT = 170

# https://note.nkmk.me/en/python-platform-system-release-version/
THEMES = {
    'Windows': 'winnative',
    'Darwin': 'aqua'
}


class MainWindow(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__()

        self.style = ttk.Style()
        pltfrm = kwargs.get('pltfrm')
        # print(f'DEBUG: {pltfrm = }; {THEMES.get(pltfrm) = }')
        self.style.theme_use(THEMES.get(pltfrm))

        self.title(f'{kwargs.get('app_name')} v{kwargs.get('app_version')}')
        # self.iconbitmap(self, ICON_FILE)
        self.always_on_top = True
        self.attributes('-topmost', self.always_on_top)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.window_width = STARTING_WINDOW_WIDTH
        self.window_height = STARTING_WINDOW_HEIGHT
        self.set_window_geometry()

        self.shift_start = kwargs.get('shift_start')
        self.shift_len = kwargs.get('shift_len')

        # Toolbar
        self.toolbar = Toolbar(master=self)

        # Expand button
        self.btn_expand_toolbar = tk.Button(
            master=self,
            text='+',
            width=0,
            height=0,
            compound='center',
            padx=0,
            pady=0,
            borderwidth=0,
            command=self.show_toolbar
        )

        # Main frame
        self.frm_main = MainFrame(
            master=self,
            shift_start=self.shift_start,
            shift_len=self.shift_len,
            borderwidth=0,
            # background='black'
        )

    def set_window_geometry(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = self.window_width
        height = self.window_height
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def show_toolbar(self):
        self.btn_expand_toolbar.grid_forget()
        self.config(menu=self.toolbar)

    def show_expand_toolbar_button(self):
        self.btn_expand_toolbar.grid(row=0, column=0, sticky='nw', padx=(0, 0), pady=(0, 0))

    def update_workday(self, shift_start, shift_len):
        self.shift_start, self.shift_len = shift_start, shift_len
        self.frm_main.frm_clock.update_workday(shift_start=shift_start, shift_len=shift_len)

    def toggle_on_top(self):
        self.always_on_top = not self.always_on_top
        self.attributes('-topmost', self.always_on_top)
        self.update()

    def run(self):
        self.show_expand_toolbar_button()
        self.frm_main.grid(row=1, column=0, sticky='nsew', padx=(5, 5), pady=(0, 0))
        self.mainloop()
