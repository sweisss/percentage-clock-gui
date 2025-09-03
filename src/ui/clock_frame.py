"""
A frame to hold the tkinter clock widgets
"""
import tkinter as tk
from datetime import datetime, timedelta

from src.ui.percentage_frame import PercentageFrame


DATETIME_FORMAT = '%H:%M:%S'


def calculate_time_percentage_of_day():
    """
    Calculate the current time as a percentage of the total time of a day (Midnight/Midnight).

    DEPRECATED in favor or more generalized and reusable function code.
    :return: Rounded float
    """
    now = datetime.now()
    seconds_of_day = now.hour * 3600 + now.minute * 60 + now.second
    percent_of_day = seconds_of_day / 86400 * 100
    return round(percent_of_day, 2)


def calculate_total_datetime_seconds(dt):
    """
    Takes a datetime object and returns its total number of seconds.

    :param dt:  Datetime object
    :return:    Int representing the total number of seconds in the datetime object
    """
    return dt.hour * 3600 + dt.minute * 60 + dt.second


def calculate_percentage_of_time_range(start, end):
    """
    Calculate the current time as a percentage of a given time range.

    :param start:   String representing the start of the time range
    :param end:     String representing the end of the time range
    :return:        Float representing the percentage of the current time within the time range
    """
    time_format = DATETIME_FORMAT
    start_time = datetime.strptime(start, time_format)
    end_time = datetime.strptime(end, time_format)

    now = datetime.now()
    current_seconds = calculate_total_datetime_seconds(now)
    start_seconds = calculate_total_datetime_seconds(start_time)
    end_seconds = calculate_total_datetime_seconds(end_time)

    percent_of_range = ( (current_seconds -  start_seconds) / (end_seconds - start_seconds) ) * 100

    return round(percent_of_range, 2)


class ClockFrame(tk.Frame):
    def __init__(self, shift_start, shift_len, **kwargs):
        super().__init__(**kwargs)

        self.shift_start = shift_start
        self.shift_len = shift_len
        self.shift_end = self.calculate_shift_end()

        # Frames
        self.frm_percent_of_total_day = PercentageFrame(master=self, text='Percent of Total Day (Midnight/Midnight)')
        self.frm_percent_of_work_day = PercentageFrame(master=self, text=f'Percent of Work Day ({self.shift_start}/{self.shift_end})')

        self.set_layout()
        self.update_time_percentage()

    def calculate_shift_end(self):
        start_dt = datetime.strptime(self.shift_start, DATETIME_FORMAT)
        end_dt = start_dt + timedelta(hours=self.shift_len)
        return end_dt.strftime(DATETIME_FORMAT)

    def set_layout(self):
        self.frm_percent_of_total_day.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.frm_percent_of_work_day.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    def update_time_percentage(self):
        percentage_of_day = calculate_percentage_of_time_range('00:00:00', '23:59:59')
        percentage_of_shift = calculate_percentage_of_time_range(self.shift_start, self.shift_end)

        self.frm_percent_of_total_day.update_time_percentage(percentage_of_day)
        self.frm_percent_of_work_day.update_time_percentage(percentage_of_shift)
        self.after(1000, self.update_time_percentage)
