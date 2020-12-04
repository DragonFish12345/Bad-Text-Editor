"""
Testing Pathlib Functions as well as Tkinter Functions :)
"""

from pathlib import Path
import tkinter as tk
import buttoncommands as cmd
import test2

add1 = test2.add1()

root = tk.Tk()

box = tk.Entry(root, bg='skyblue')
box.pack()

button = tk.Button(root, text='add 1', command=add1)
button.pack()

root.mainloop()