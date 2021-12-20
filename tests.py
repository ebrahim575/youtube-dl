# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
#
# ttk.Style().configure('green/black.TButton',  background='#007AFF')
#
# button = ttk.Button(root, text='Click Me!', style='green/black.TButton')
# button.pack()
#
# root.mainloop()
from tkinter import *
from tkmacosx import Button

root = Tk()

B1 = Button(root, text='Mac OSX')
B1.pack()

root.mainloop()