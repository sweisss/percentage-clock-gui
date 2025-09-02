"""
A frame to hold the tkinter clock widgets
"""
import tkinter as tk
from datetime import datetime

from src.ui.progress_bar_frame import ProgressBarFrame
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
        self.frm_progress_bar = ProgressBarFrame(master=self)

        self.set_layout()
        self.update_time_percentage()

    def set_layout(self):
        self.frm_time_perc_display.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.frm_progress_bar.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    def update_time_percentage(self):
        time_percentage = calculate_time_percentage()
        self.frm_time_perc_display.update_label_text(time_percentage)
        self.frm_progress_bar.update_progress(time_percentage)
        self.after(1000, self.update_time_percentage)
