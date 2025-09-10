"""
A toolbar menu widget for the main window.
"""
import tkinter as tk
from tkinter import messagebox

from src.ui.edit_workday_popup import EditWorkdayWindow


ABOUT_MSG = ('This app is written in python 3.12.3 under the MIT licence.\n'
            '---------------------------------------------------------------------------\n'
            '\n'
            'MIT License\n'
            '\n'
            'Copyright (c) 2025 Seth Weiss\n'
            '\n'
            'Permission is hereby granted, free of charge, to any person obtaining a copy'
            'of this software and associated documentation files (the "Software"), to deal'
            'in the Software without restriction, including without limitation the rights'
            'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell'
            'copies of the Software, and to permit persons to whom the Software is'
            'furnished to do so, subject to the following conditions:\n'
            '\n'
            'The above copyright notice and this permission notice shall be included in all'
            'copies or substantial portions of the Software.\n'
            '\n'
            'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR'
            'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,'
            'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE'
            'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER'
            'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
            'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE'
            'SOFTWARE.')

USAGE = ('To edit the Work Day time range:\n'
          '- Click on Edit > Edit Work Day\n'
          '- Enter a starting time and a shift duration\n'
         '\n'
         'To toggle the "Always On Top" feature:\n'
         '- Click on View > Toggle Always On Top\n'
         '\n'
         'To hide the toolbar:\n'
         '- Click on View > Hide Toolbar\n'
         '- Alternatively, click on the "-" button\n'
         '- Click on the "+" button to show the toolbar again')


class Toolbar(tk.Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_window = self.master

        # Menus
        self.menu_file = tk.Menu(self.main_window, tearoff=0)
        self.menu_edit = tk.Menu(self.main_window, tearoff=0)
        self.menu_view = tk.Menu(self.main_window, tearoff=0)
        self.menu_help = tk.Menu(self.main_window, tearoff=0)

        # Labels
        self.toggle_indicator = '  ✔️'
        self.always_on_top_base = 'Toggle Always On Top'
        self.lbl_always_on_top = tk.StringVar(
            master=self.menu_view,
            value=self.always_on_top_base + self.toggle_indicator
        )

        self.set_menus()

    ###### File Menu ######
    def set_file_menu(self):
        self.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='Exit', command=self.quit)

    ###### Edit Menu ######
    def on_edit_window_close(self, event):
        if event.widget == event.widget.winfo_toplevel():
            if event.widget.updated_data:
                self.main_window.update_workday(
                    event.widget.updated_data.get('start_time'),
                    event.widget.updated_data.get('duration')
                )

    def open_edit_workday_popup(self):
        edit_workday_window = EditWorkdayWindow(
            geometry=self.main_window.winfo_geometry(),
            shift_start=self.main_window.shift_start,
            shift_len=self.main_window.shift_len
        )
        edit_workday_window.bind('<Destroy>', self.on_edit_window_close)

    def set_edit_menu(self):
        self.add_cascade(label='Edit', menu=self.menu_edit)
        self.menu_edit.add_command(
            label='Edit Work Day',
            command=self.open_edit_workday_popup
        )

    ###### View Menu ######
    def toggle_topview(self):
        self.main_window.toggle_on_top()
        toggled = self.toggle_indicator if self.main_window.always_on_top else ''
        self.lbl_always_on_top.set(self.always_on_top_base + toggled)
        self.menu_view.entryconfig(1, label=self.lbl_always_on_top.get())

    def hide_toolbar(self):
        self.main_window.config(menu='')
        self.main_window.toggle_toolbar()

    def set_view_menu(self):
        self.add_cascade(label='View', menu=self.menu_view)
        self.menu_view.add_cascade(
            label='Hide Toolbar',
            command=self.hide_toolbar
        )
        self.menu_view.add_cascade(
            label=self.lbl_always_on_top.get(),
            command=self.toggle_topview
        )

    ###### Help Menu ######
    def display_about_message(self):
        messagebox.showinfo(
            title=self.main_window.title(),
            message=ABOUT_MSG,
        )

    def display_usage(self):
        messagebox.showinfo(
            title='Usage',
            message=USAGE
        )

    def set_help_menu(self):
        self.add_cascade(label='Help', menu=self.menu_help)
        self.menu_help.add_command(
            label='About',
            command=self.display_about_message,
        )
        self.menu_help.add_command(
            label='Usage',
            command=self.display_usage
        )

    ###### Set Menus ######
    def set_menus(self):
        self.set_file_menu()
        self.set_edit_menu()
        self.set_view_menu()
        self.set_help_menu()
