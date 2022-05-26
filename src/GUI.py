# %%
from pydoc import importfile
from tkinter import *

# %%
root = Tk()
root.geometry("800x800")

# Title label widget
titleScreen = Label(root, text="Carpedia")
titleScreen.pack()

# Carpedia logo widget
logo = PhotoImage(file='./assets/logo.gif')
logoLabel = Label(root, image=logo)
logoLabel.pack()

root.mainloop()
