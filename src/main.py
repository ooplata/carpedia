# %%
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pydoc import importfile
from tkinter import *

from cars.cars import ImportedCar

# %%
file = open('assets/Cars.json')
data = json.load(file)

cars = []

# %%
for car in data["Imported"]:
    c = ImportedCar(car)
    cars.append(c)

# %%
file.close()

# %%
root = Tk()
root.geometry("600x600")

# Title label widget
titleScreen = Label(root, text="Carpedia")
titleScreen.pack()

# Carpedia logo widget
logo = PhotoImage(file='assets/logo.gif')
logoLabel = Label(root, image=logo)
logoLabel.pack()

root.mainloop()
