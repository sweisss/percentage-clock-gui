"""
Frame to hold the time display label.
"""
import tkinter as tk
from tkinter import ttk


class TimeDisplayFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Labels
        self.lbl_time = ttk.Label(master=self, text='Hello, World!')

        self.set_layout()

    def set_layout(self):
        self.lbl_time.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
