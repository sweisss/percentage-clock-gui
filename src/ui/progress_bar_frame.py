"""
Frame to hold the tkinter progress bar widget
"""
import tkinter as tk
from tkinter import ttk


PROGRESS_BAR_WIDTH = 400


class ProgressBarFrame(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Progress Bar
        self.progress = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(master=self, length=PROGRESS_BAR_WIDTH, variable=self.progress)

        self.set_layout()

    def set_layout(self):
        self.progress_bar.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def update_progress(self, decimal):
        self.progress.set(decimal)
