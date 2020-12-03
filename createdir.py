from pathlib import Path

"""
Creates a directory in C:\\Users\\user home directory
"""

def create_directory():
    homedir = Path.home()
    newdir = Path(f'{homedir}\\1files')
    newdir.mkdir()


