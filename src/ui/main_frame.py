"""
The main frame of the app GUI, used to organize all sub-frames and UI features
"""
import tkinter as tk

from src.ui.time_display_frame import TimeDisplayFrame


class MainFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Frames
        self.frm_time_readout = TimeDisplayFrame(master=self)
        # self.frm_progress_bar = ...

        self.set_layout()

    def set_layout(self):
        self.frm_time_readout.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
