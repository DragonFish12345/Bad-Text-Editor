import tkinter as tk
import os
from pathlib import Path

def deletefile():
    filedir = f'{Path.home()}\\1files'
    path = Path(filedir)
    a = path.glob('*')
    list = ''
    for x in a:
        x = str(x)
        list += x
        list += '\n'

deletefile()
