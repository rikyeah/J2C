import os
from tkinter import *
from src.main import main
from tkinter import filedialog, messagebox

resource_path = ""


def choose_file():
    global resource_path
    resource_path = filedialog.askopenfile(initialdir="C://", title="J2C - Choose a file")
    resource_path_label.configure(text=resource_path)
    print(resource_path.name)


def choose_dir():
    global resource_path
    resource_path = filedialog.askdirectory(initialdir="C://", title="J2C - Choose a directory")
    resource_path_label.configure(text=resource_path)
    print(resource_path)


root = Tk()
root.geometry("450x200")
root.title("J2C")
title = Label(root, text="J2C - Java to C converter")
title.pack()
resource_path_label = Label(root, text="no file or directory selected")
resource_path_label.pack(side=LEFT)
choose_file_button = Button(root, text="Choose file", command=choose_file)
choose_file_button.pack(side=RIGHT)
choose_directory_button = Button(root, text="Choose directory", command=choose_dir)
choose_directory_button.pack(side=RIGHT)


def start_translation():
    global resource_path
    if resource_path == "":
        messagebox.showerror("Error", "No file or directory selected")
    elif not os.path.exists(resource_path):
        messagebox.showerror("Error", "File {} doesn't exist".format(resource_path))
    main(resource_path)


translate_button = Button(root, text="Translate", command=start_translation)
translate_button.pack(side=BOTTOM)

root.mainloop()
