"""
Testing Pathlib Functions as well as Tkinter Functions :)
"""

from pathlib import Path
import tkinter as tk
import buttoncommands as cmd

root = tk.Tk()

hi = tk.Button(root, text='asdjf', command=cmd.deletefile)
hi.pack()

root.mainloop()