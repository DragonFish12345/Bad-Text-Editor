import tkinter as tk
import os
from pathlib import Path

def deletefile():
    i = 0
    filedir = f'{Path.home()}\\1files'
    path = Path(filedir)
    a = path.glob('*')
    list = ''
    for x in a:
        x = str(x)
        x = x.replace(f'{filedir}\\', '')
        list += x
        list += ', '
        i += 1
        if i%3 == 0:
            list += '\n'

    promptlabel = tk.Label(text=f'You can delete these files:\n{list}\nWhich file do you want to delete?', bg='skyblue')
    promptlabel.pack()
    file_delete_choice = promptlabel.get()
    prompt1 = tk.Label(text=f'Do you really want to delete {file_delete_choice}?')
    prompt1.pack()
    buttonyes = tk.Button(text='yes')
    buttonno = tk.Button(text='no')
    buttonyes.pack()
    buttonno.pack()

