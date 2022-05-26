
from pydoc import importfile
from tkinter import *
import sys
sys.path.insert(0, 'C:\\Users\\Rog Strix\\OneDrive\\Documentos\\carpedia\\src\\assets')


root = Tk()
root.geometry("800x800")

#Title lable widget
titleScreen = Label(root, text="Carpedia")
titleScreen.pack()

#Carpedia logo widget
logo = PhotoImage(file= './assets/logo.gif')
logoLabel = Label(root, image= logo)
logoLabel.pack()

root.mainloop()
