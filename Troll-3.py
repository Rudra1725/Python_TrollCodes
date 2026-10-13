import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

CLICK_LIMIT = 8
clicks = 0

while clicks < CLICK_LIMIT:
    messagebox.showerror(
        "Critical Kernel Error 0x80070002",
        "Memory leak detected in module C:\\System32\\driver.sys.\n\n"
        "Click OK to isolate the corrupted sector."
    )
    clicks += 1
messagebox.showinfo("Gotcha!", "Prank over — your laptop is completely fine.")
