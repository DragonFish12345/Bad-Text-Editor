"""
Testing Pathlib Functions as well as Tkinter Functions :)
"""

from pathlib import Path
import tkinter as tk
import buttoncommands as cmd
import test2


root = tk.Tk()

box = tk.Entry(root, bg='skyblue')
box.pack()

button = tk.Button(root, text='add 1')
button.pack()

for child in root.winfo_children():
    child.destroy()

root.mainloop()