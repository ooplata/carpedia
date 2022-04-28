# %%
import json
from cars.cars import ImportedCar

# %%
file = open('Cars.json')
data = json.load(file)

for car in data["Imported"]:
    c = ImportedCar(car)
    print(c.model)

file.close()
# %%
