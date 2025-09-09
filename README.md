# Percentage Clock
A simple desktop GUI to display the current time as a percentage throught the day.

<img width="515" height="207" alt="image" src="https://github.com/user-attachments/assets/935e1200-42e7-4249-ac3d-960968067dbf" />

The clock displays the current time as a percentage of two different time ranges:
- Total Day - Starting and ending at midnight
- Work Day - The start time and duration of a work shift set by the user

The user can edit the Work Day via the hidden toolbar,
which can be expanded by pressing the "+" button at the top-left of the GUI.

The GUI defaults to "Always On Top" which keeps it above all other windows.
This feature can be toggled in the "View" menu of the toolbar.

This program was made only with features of the python base library and therefore has no external dependencies and
is not packaged as an executable. To run the program, clone this repo to the directory of choice,
`cd` into the top level of the project, and enter:
```commandline
python main.py
```

Alternatively, the application takes two optional arguments for Work Day start time and duration.
These arguments can be added to the above command. Another trick to get the benefits of a packaged executable
without installing [pyinstaller](https://pyinstaller.org/en/stable/) is to make a _.bat_ file in the project's
top-level directory and save a shortcut to this _.bat_ file on the Desktop. The _.bat_ file can read something like:
```commandline
start /MIN py C:\Path\To\Your\Project\main.py <shift_start> <shift_length>
```

In the above command, the `/MIN` command minimizes the background console window that spawns the GUI.
The python command `py` can be replaced with `python`, `python3`, `python3.12` or whichever version is
appropriate for the local environment. 

While this application will work on multiple operating systems, it is targeted towards Windows.
It therefore may have some bugs on other systems. 

This application was written in python 3.12.3
