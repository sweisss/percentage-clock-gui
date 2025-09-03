"""
Popup window to edit the details of the workday.
"""
import tkinter as tk


class EditWorkdayWindow(tk.Toplevel):
    def __init__(self, geometry, **kwargs):
        super().__init__(**kwargs)

        self.title('Edit Work Day')
        self.resizable(False, False)
        self.grab_set()
        # self.iconbitmap(ICON_FILE)

        self.set_window_geometry(main_window_geometry=geometry)

    def set_window_geometry(self, main_window_geometry=None, width=350, height=300):
        parent_geometry_parts = main_window_geometry.split('+')
        parent_left_edge = parent_geometry_parts[1]
        parent_top_edge = parent_geometry_parts[2]
        parent_height = parent_geometry_parts[0].split('x')[1]
        parent_width = parent_geometry_parts[0].split('x')[0]
        window_left_edge = int(parent_left_edge) + int(parent_width) / 4
        window_top_edge = int(parent_top_edge) + int(parent_height) / 4
        self.geometry('%dx%d+%d+%d' % (width, height, window_left_edge, window_top_edge))

    def close_window(self):
        self.destroy()
