# %%
class Internals:
    def __init__(self, json):
        self.engine = Engine(json["engine"])
        self.transmission = json["transmission"]
        self.fourWd = json["4WD"]
        self.powerTrain = json["powerTrain"]
        self.fuelType = json["fuelType"]
        self.fuelConsumption = json["fuelConsumption"]


# %%
class Engine:
    def __init__(self, json):
        self.size = json["size"]
        self.cylinders = json["cylinders"]
        self.inductionType = json["inductionType"]
        self.horsePower = json["horsePower"]
        self.torque = json["torque"]

# %%
