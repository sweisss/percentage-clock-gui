"""
The main frame of the app GUI, used to organize all sub-frames and UI features
"""
import tkinter as tk

from src.ui.clock_frame import ClockFrame


class MainFrame(tk.Frame):
    def __init__(self, shift_range, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_clock = ClockFrame(master=self, shift_range=shift_range)

        self.set_layout()

    def set_layout(self):
        self.frm_clock.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
