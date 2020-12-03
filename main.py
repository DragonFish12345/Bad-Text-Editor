import createdir
from pathlib import Path
import tkinter as tk
import buttoncommands as cmd

home_dir = Path.home()
files_dir = Path(f'{home_dir}\\1files')

if not files_dir.exists():
    createdir.create_directory()

root = tk.Tk()
root.title('1 Text Editor')
root.geometry('500x500')

welcome_label = tk.Label(root, text='1 Text Editor\nThe Worst Text Editor in World of Programming', bg='sky blue')
welcome_label.pack()

openchoice = tk.Button(root, text='Open File', padx=30)
deletechoice = tk.Button(root, text='Delete a file', padx=30, command=cmd.deletefile)
newchoice = tk.Button(root, text='New File', padx=30)

newchoice.pack()
openchoice.pack()
deletechoice.pack()




root.mainloop()