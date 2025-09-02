"""
A frame to hold the tkinter clock widgets
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime

from src.ui.time_display_frame import TimeDisplayFrame


def calculate_time_percentage():
    now = datetime.now()
    seconds_of_day = now.hour * 3600 + now.minute * 60 + now.second
    percent_of_day = seconds_of_day / 86400 * 100
    return round(percent_of_day, 4)


class ClockFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_time_perc_display = TimeDisplayFrame(master=self)
        self.frm_progress_bar = ...

        self.set_layout()
        self.update_time_percentage()

    def set_layout(self):
        self.frm_time_perc_display.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def update_time_percentage(self):
        self.frm_time_perc_display.update_label_text(calculate_time_percentage())
        self.after(1000, self.update_time_percentage)
