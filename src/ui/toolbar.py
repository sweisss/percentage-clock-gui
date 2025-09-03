"""
A toolbar menu widget for the main window.
"""
import tkinter as tk


class Toolbar(tk.Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Menus
        self.menu_file = tk.Menu(self.master, tearoff=0)
        self.menu_edit = tk.Menu(self.master, tearoff=0)
        self.menu_view = tk.Menu(self.master, tearoff=0)
        self.menu_help = tk.Menu(self.master, tearoff=0)

        self.set_menus()

    def set_file_menu(self):
        self.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='Exit', command=self.quit)

    def set_edit_menu(self):
        self.add_cascade(label='Edit', menu=self.menu_edit)
        self.menu_edit.add_command(
            label='Nothing here yet',
            command=lambda: print('No Edit command yet')
        )

    def hide_toolbar(self):
        self.master.config(menu='')
        self.master.show_expand_toolbar_button()

    def set_view_menu(self):
        self.add_cascade(label='View', menu=self.menu_view)
        self.menu_view.add_cascade(
            label='Hide toolbar',
            command=self.hide_toolbar
        )

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

    def set_menus(self):
        self.set_file_menu()
        self.set_edit_menu()
        self.set_view_menu()
        self.set_help_menu()
