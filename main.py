from tkinter import *
from tkinter import ttk
import tkinter as tk
import items
import tkmacosx

root = tk.Tk()
root.title("Melvor Calculator")
root.resizable(True, True)
root.iconbitmap('img/logo_no_text.png')
style = ttk.Style()
style.theme_use("aqua")

tabControl = ttk.Notebook(root)


tab1 = Frame(tabControl)
tabControl.add(tab1, text='Woodcutting')
tabControl.place(x=0, y=0)


root.mainloop()