# %%
from cars.cars import ImportedCar
from ui.tkcore import Application

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import *


# %%
class App(Application):
    def __init__(self) -> None:
        super().__init__("Carpedia", "assets/logo.gif", "600x600")

    def onstartup(self):
        file = open('assets/Cars.json')
        data = json.load(file)

        cars = []
        for car in data["Imported"]:
            c = ImportedCar(car)
            cars.append(c)

        file.close()
        lb = Listbox(self.window)
        for car in cars:
            lb.insert(END, car)
        lb.pack()

    def onclosure(self):
        print("Thanks for using Carpedia!")

# %%
