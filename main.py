import createdir
from pathlib import Path
import tkinter as tk
import buttoncommands as cmd

home_dir = Path.home()
files_dir = Path(f'{home_dir}\\1files')

if not files_dir.exists():
    createdir.create_directory()

root = tk.Tk()

# Defining a function that clears the board

deletefile = cmd.deletefile
createfile = cmd.createfile

def refreshboard():
    for child in root.winfo_children():
        child.destroy()

    welcome_label = tk.Label(root, text='1 Text Editor\nThe Worst Text Editor in World of Programming', bg='sky blue')
    welcome_label.pack()

    clear_board_button = tk.Button(root, text='Clear Screen (Removes notices)', bg='yellow', command=refreshboard)
    clear_board_button.pack()

    openchoice = tk.Button(root, text='Open File', padx=30)
    deletechoice = tk.Button(root, text='Delete a file', padx=30, command=deletefile)
    newchoice = tk.Button(root, text='New File', padx=30, command=createfile)

    newchoice.pack()
    openchoice.pack()
    deletechoice.pack()


root.title('1 Text Editor')
root.geometry('700x700')

welcome_label = tk.Label(root, text='1 Text Editor\nThe Worst Text Editor in World of Programming', bg='sky blue')
welcome_label.pack()

clear_board_button = tk.Button(root, text='Clear Screen (Removes notices)', bg='yellow', command=refreshboard)
clear_board_button.pack()

openchoice = tk.Button(root, text='Open File', padx=30)
deletechoice = tk.Button(root, text='Delete a file', padx=30, command=deletefile)
newchoice = tk.Button(root, text='New File', padx=30, command=createfile)

newchoice.pack()
openchoice.pack()
deletechoice.pack()





root.mainloop()