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

        # Frames
        self.frm_entries = tk.Frame(master=self)
        self.frm_buttons = tk.Frame(master=self)

        # Labels
        self.lbl_start_time_title = tk.Label(master=self.frm_entries, text='Start Time')
        self.lbl_min_divider = tk.Label(master=self.frm_entries, text=':')
        self.lbl_duration_title = tk.Label(master=self.frm_entries, text='Duration (hrs)')

        # Entries
        self.ent_start_time_hrs = tk.Entry(master=self.frm_entries, justify=tk.RIGHT, width=3)
        self.ent_start_time_mins = tk.Entry(master=self.frm_entries, width=3)
        self.ent_duration = tk.Entry(master=self.frm_entries, width=3)

        # Buttons
        self.btn_save = tk.Button(
            master=self.frm_buttons,
            text='Save',
            command=lambda: print('Save button was pressed')
        )
        self.btn_cancel = tk.Button(
            master=self.frm_buttons,
            text='Cancel',
            command=lambda: print('Cancel button was pressed')
        )

        self.set_window_geometry(main_window_geometry=geometry)
        self.set_layout()

    def set_window_geometry(self, main_window_geometry=None, width=350, height=100):
        parent_geometry_parts = main_window_geometry.split('+')
        parent_left_edge = parent_geometry_parts[1]
        parent_top_edge = parent_geometry_parts[2]
        parent_height = parent_geometry_parts[0].split('x')[1]
        parent_width = parent_geometry_parts[0].split('x')[0]
        window_left_edge = int(parent_left_edge) + int(parent_width) / 4
        window_top_edge = int(parent_top_edge) + int(parent_height) / 4
        self.geometry('%dx%d+%d+%d' % (width, height, window_left_edge, window_top_edge))

    def set_layout(self):
        self.frm_entries.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.lbl_start_time_title.grid(row=0, column=0, sticky='nsew', padx=(5, 0), pady=5)
        self.ent_start_time_hrs.grid(row=0, column=1, sticky='nsew', padx=(0, 0), pady=5)
        self.lbl_min_divider.grid(row=0, column=2, sticky='nsew', padx=(0, 0), pady=5)
        self.ent_start_time_mins.grid(row=0, column=3, sticky='nsew', padx=(0, 5), pady=5)

        self.lbl_duration_title.grid(row=0, column=4, sticky='nsew', padx=(10, 0), pady=5)
        self.ent_duration.grid(row=0, column=5, sticky='nsew', padx=(0, 5), pady=5)

        self.frm_buttons.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        self.btn_save.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.btn_cancel.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

    def close_window(self):
        self.destroy()
