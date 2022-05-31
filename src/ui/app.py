# %%
from cars.cars import Car, ImportedCar
from ui.tkcore import Application

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk


# %%
class App(Application):
    def __init__(self) -> None:
        super().__init__("Carpedia", "assets/Logo.ico", "600x600")
        self.cars = []

    def onstartup(self):
        file = open('assets/Cars.json')
        data = json.load(file)

        for car in data["Imported"]:
            c = ImportedCar(car)
            self.cars.append(c)

        file.close()
        lb = tk.Listbox(self.window)
        for car in self.cars:
            lb.insert(tk.END, car)

        lb.bind('<<ListboxSelect>>', self.onselect)
        lb.pack(fill="x", side="top")

        self.info = tk.Text(self.window)
        self.info.insert(tk.INSERT, "Select a car to see more")
        self.info.pack(fill="x", side="bottom")

    def onselect(self, evt):
        w = evt.widget
        sel = w.curselection()
        if (sel != None):
            index = sel[0]
            car = self.cars[index]

            infoStr = f"{car.model} by {car.brand}\n"
            infoStr += f"Released on {car.releaseYear}"
            infoStr += f", imported on {car.importedOn}\n"
            infoStr += f"Body type: {car.body}\n\n"

            infoStr += f"Internals\n"
            infoStr += f"Transmission: {car.internals.transmission}\n"
            infoStr += f"4WD: {car.internals.fourWd}\n"
            infoStr += f"Power train: {car.internals.powerTrain}\n"
            infoStr += f"Fuel type: {car.internals.fuelType}\n"
            infoStr += f"Fuel consumption: {car.internals.fuelConsumption}\n\n"

            infoStr += f"Engine\n"
            infoStr += f"Size: {car.internals.engine.size}\n"
            infoStr += f"Cylinders: {car.internals.engine.cylinders}\n"
            infoStr += f"Induction type: {car.internals.engine.inductionType}\n"
            infoStr += f"Horse power: {car.internals.engine.horsePower}\n"
            infoStr += f"Torque: {car.internals.engine.torque}\n"

            self.info.delete(1.0, tk.END)
            self.info.insert(tk.INSERT, "About")

            self.showPriceGraph(car)

    def showPriceGraph(self, car: Car):
        prices = car.priceHistory.items()
        x, y = zip(*prices)
        plt.plot(x, y, marker='o')
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title(car)
        plt.show()

    def onclosure(self):
        print("Thanks for using Carpedia!")

# %%
