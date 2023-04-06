import tkinter as tk
from tkinter import *

root = tk.Tk()

def clear_entry():
    entry.delete(0, END)

entry = Entry()
entry.grid(row=0, column=1)

button = Button(root, text="Clear", command=clear_entry)
button.grid(row=1, column=1)

root.mainloop()