"""
A frame to hold the tkinter clock widgets
"""
import tkinter as tk
from datetime import datetime

from src.ui.percent_of_day_frame import PercentOfDayFrame


def calculate_time_percentage_of_day():
    now = datetime.now()
    seconds_of_day = now.hour * 3600 + now.minute * 60 + now.second
    percent_of_day = seconds_of_day / 86400 * 100
    return round(percent_of_day, 4)


class ClockFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_percent_of_day = PercentOfDayFrame(master=self, text='Percent of Total Day (Midnight/Midnight)')

        self.set_layout()
        self.update_time_percentage()

    def set_layout(self):
        self.frm_percent_of_day.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def update_time_percentage(self):
        time_percentage = calculate_time_percentage_of_day()
        self.frm_percent_of_day.update_time_percentage(time_percentage)
        self.after(1000, self.update_time_percentage)
