"""
A frame to hold the tkinter widgets responsible for the percentage of the day.
"""
import tkinter as tk
from tkinter import ttk

from src.ui.progress_bar_frame import ProgressBarFrame
from src.ui.time_display_frame import TimeDisplayFrame


class PercentageFrame(ttk.LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_time_perc_display = TimeDisplayFrame(master=self)
        self.frm_progress_bar = ProgressBarFrame(master=self)

        self.set_layout()

    def set_layout(self):
        self.frm_time_perc_display.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.frm_progress_bar.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

    def update_time_percentage(self, time_percentage):
        self.frm_time_perc_display.update_label_text(time_percentage)
        self.frm_progress_bar.update_progress(time_percentage)
