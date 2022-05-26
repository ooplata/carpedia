# %%
from cars.cars import Car, ImportedCar
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

    def showPriceGraph(self, car: Car):
        prices = car.priceHistory.items()
        x, y = zip(*prices)
        plt.plot(x, y)
        plt.plot(x, y, marker='o')
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title(c.model)
        plt.show()

    def onstartup(self):
        file = open('assets/Cars.json')
        data = json.load(file)

        cars = []
        for car in data["Imported"]:
            c = ImportedCar(car)
            cars.append(c)
            self.showPriceGraph(c)

        file.close()
        lb = Listbox(self.window)
        for car in cars:
            lb.insert(END, car)
        lb.pack()

    def onclosure(self):
        print("Thanks for using Carpedia!")

# %%
