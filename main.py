import createdir
from pathlib import Path
import tkinter as tk
import buttoncommands as cmd

home_dir = Path.home()
files_dir = Path(f'{home_dir}\\1files')
path = f'{home_dir}\\1files'

if not files_dir.exists():
    createdir.create_directory()

root = tk.Tk()

# Storing functions in buttoncommands.py into local file
allfiles = cmd.allfiles
deletefile = cmd.deletefile
createfile = cmd.createfile
openfile = cmd.openfile
_from_rgb = cmd._from_rgb


# Instructions on how to use the text editor

def instructions():
    for child in root.winfo_children():
        child.destroy()

    s = f"""
    This text editor works like any other text editor, except it's just worse. All files created and deleted
    are in a folder in your home directory. The folder is called 1files, and the absolute directory
    is {Path.home}\\1files. This editor can't undo, and once it's saved, it's there forever.
    """
    instructions_label = tk.Label(root, text=s, bg=_from_rgb((32, 237, 59)))
    instructions_label.pack()
    back_button = tk.Button(root, text='Back', bg=_from_rgb((48, 209, 249)), command=refreshboard)
    back_button.pack()


# Defining a function that clears the board
def refreshboard():
    for child in root.winfo_children():
        child.destroy()

    welcome_label = tk.Label(root, text='1 Text Editor\nThe Worst Text Editor in World of Programming', bg='sky blue')
    welcome_label.pack()

    clear_board_button = tk.Button(root, text='Clear Screen (Removes notices)', bg='yellow', command=refreshboard)
    clear_board_button.pack()

    file_button = tk.Button(root, text=f'All files under the {path} directory', command=allfiles)
    file_button.pack()

    instruction_button = tk.Button(root, text='Instructions', command=instructions)
    instruction_button.pack()

    openchoice = tk.Button(root, text='Open File', padx=30, command=openfile)
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

file_button = tk.Button(root, text=f'All files under the {path} directory', command=allfiles)
file_button.pack()

instruction_button = tk.Button(root, text='Instructions', command=instructions)
instruction_button.pack()

openchoice = tk.Button(root, text='Open File', padx=30, command=openfile)
deletechoice = tk.Button(root, text='Delete a file', padx=30, command=deletefile)
newchoice = tk.Button(root, text='New File', padx=30, command=createfile)

newchoice.pack()
openchoice.pack()
deletechoice.pack()





root.mainloop()
