# %%
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from cars.cars import ImportedCar

# %%
file = open('Cars.json')
data = json.load(file)

# %%
for car in data["Imported"]:
    c = ImportedCar(car)

    prices = c.priceHistory.items()
    x, y = zip(*prices)
    plt.plot(x, y, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.title(c.model)
    plt.show()

# %%
file.close()
