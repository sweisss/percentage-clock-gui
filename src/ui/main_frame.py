"""
The main frame of the app GUI, used to organize all sub-frames and UI features
"""
import tkinter as tk

from src.ui.clock_frame import ClockFrame


class MainFrame(tk.Frame):
    def __init__(self, shift_start, shift_len, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_clock = ClockFrame(
            master=self,
            shift_start=shift_start,
            shift_len=shift_len,
            borderwidth=0,
            # background='red'
        )

        self.set_layout()

    def set_layout(self):
        self.frm_clock.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)
