import tkinter as tk
import os
from pathlib import Path
from time import sleep

def deletefile():
    i = 0
    filedir = f'{Path.home()}\\1files'
    path = Path(filedir)
    a = path.glob('*')
    list = ''
    allfiles = []
    for x in a:
        x = str(x)
        x = x.replace(f'{filedir}\\', '')
        list += x
        list += ', '
        i += 1
        if i%3 == 0:
            list += '\n'
        allfiles.append(x)

    if list == '':
        list = 'You have no files currently in your C:\\Users\\*user\\1files directory! Why not create a new file?'
    promptlabel = tk.Label(text=f'You can delete these files:\n{list}\nWhich file do you want to delete?', bg='skyblue')
    promptlabel.pack()
    file_delete_box = tk.Entry(bg='silver')
    file_delete_box.pack()
    file_delete_choice = ''

    def continuewithdelete():
        file_delete_choice = file_delete_box.get()
        fileexists = ''
        for x in allfiles:
            x = str(x)
            if x == file_delete_choice:
                fileexists = True
                break

        def actuallydeleting():
            os.remove(f'{filedir}\\{file_delete_choice}')
            afterdeleted = tk.Label(text=f'{file_delete_choice} deleted. Click the Clear Screen to clear the screen.')
            afterdeleted.pack()
            sleep(3)

        if not fileexists:
            doesntexist = tk.Label(text=f'{file_delete_choice} DOES NOT EXIST')
            doesntexist.pack()
        else:
            confirmlabel = tk.Label(text=f'Are you sure you want to delete {file_delete_choice}?')
            confirmlabel.pack()
            buttonyes = tk.Button(text='yes', bg='green', command=actuallydeleting)
            buttonno = tk.Button(text='no', bg='red')
            buttonyes.pack()
            buttonno.pack()

    okay_button = tk.Button(text='Continue', bg='green', command=continuewithdelete)
    okay_button.pack()



