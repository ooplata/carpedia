# %%
from cars.engine import Engine


# %%
# Definición de la clase
class Internals:
    def __init__(self, json):
        self.engine = Engine(json["engine"])
        self.transmission = json["transmission"]
        self.diff = json["4WD"]
        self.powerTrain = json["powerTrain"]
        self.fuelType = json["fuelType"]
        self.fuelConsumption = json["fuelConsumption"]

# %%
