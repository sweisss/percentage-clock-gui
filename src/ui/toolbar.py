"""
A toolbar menu widget for the main window.
"""
import tkinter as tk

from src.ui.edit_workday_popup import EditWorkdayWindow


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
        self.main_window.show_expand_toolbar_button()

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
    def set_help_menu(self):
        self.add_cascade(label='Help', menu=self.menu_help)
        self.menu_help.add_command(
            label='About',
            command=lambda: print('No About command yet'),
        )
        self.menu_help.add_command(
            label='User Guide',
            command=lambda: print('No User Guide command yet')
        )

    ###### Set Menus ######
    def set_menus(self):
        self.set_file_menu()
        self.set_edit_menu()
        self.set_view_menu()
        self.set_help_menu()
