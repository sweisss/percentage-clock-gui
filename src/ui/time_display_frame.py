"""
Frame to hold the time display label.
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime


class TimeDisplayFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Labels
        self.lbl_time = ttk.Label(master=self, text=f'{self.calculate_time_percentage()}%')

        self.set_layout()

    def set_layout(self):
        self.lbl_time.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def calculate_time_percentage(self):
        now = datetime.now()
        print(f'DEBUG: {now.hour = }; {now.minute = }; {now.second = }')
        seconds_of_day = now.hour * 3600 + now.minute * 60 + now.second
        print(f'DEBUG: {seconds_of_day = }')
        percent_of_day = seconds_of_day / 86400 * 100
        print(f'DEBUG: {percent_of_day = }')
        return round(percent_of_day, 4)
