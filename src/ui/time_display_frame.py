"""
Frame to hold the time display label.
"""
import tkinter as tk
from tkinter import ttk


class TimeDisplayFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Labels
        self.lbl_time_percent = ttk.Label(master=self, text=f'00.0000%')

        self.set_layout()

    def set_layout(self):
        self.lbl_time_percent.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def update_label_text(self, txt):
        self.lbl_time_percent.configure(text=f'{txt:.4f}%')
