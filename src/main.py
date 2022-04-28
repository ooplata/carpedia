# %%
import json
from cars.cars import ImportedCar
from cars.engine import Engine
from cars.internals import Internals

# %%
file = open('Cars.json')
data = json.load(file)

for car in data["Imported"]:
    print(car)

file.close()
# %%
