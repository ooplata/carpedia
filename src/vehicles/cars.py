# %%
from abc import ABC, abstractmethod
from vehicles.internals import Internals


# %%
# Definición de las clases
class Car(ABC):
    def __init__(self, json):
        self.releaseYear = json["releaseYear"]
        self.model = json["model"]
        self.brand = json["brand"]
        self.body = json["body"]
        self.priceHistory = json["priceHistory"]
        self.internals = Internals(json["internals"])

    def __str__(self):
        return self.model + " by " + self.brand + " (" + self.releaseYear.__str__() + ")"

    @abstractmethod
    def short_description(self) -> str:
        return f"{self.model} by {self.brand} ({self.releaseYear})"

    @abstractmethod
    def long_description(self) -> str:
        infoStr = f"{self.model} by {self.brand}\n"
        infoStr += f"Release year: {self.releaseYear}\n"
        infoStr += f"Body type: {self.body}\n\n"

        infoStr += f"Internals\n"
        infoStr += f"Transmission: {self.internals.transmission}\n"
        infoStr += f"4WD: {self.internals.fourWd}\n"
        infoStr += f"Power train: {self.internals.powerTrain}\n"
        infoStr += f"Fuel type: {self.internals.fuelType}\n"
        infoStr += f"Fuel consumption: {self.internals.fuelConsumption}\n\n"

        infoStr += f"Engine\n"
        infoStr += f"Size: {self.internals.engine.size}\n"
        infoStr += f"Cylinders: {self.internals.engine.cylinders}\n"
        infoStr += f"Induction type: {self.internals.engine.inductionType}\n"
        infoStr += f"Horse power: {self.internals.engine.horsePower}\n"
        infoStr += f"Torque: {self.internals.engine.torque}\n"
        return infoStr


class ImportedCar(Car):
    def __init__(self, json):
        self.importedOn = json["importedOn"]
        self.originCountry = json["originCountry"]
        super().__init__(json)


class NewCar(Car):
    def __init__(self, json):
        self.dealership = json["dealership"]
        super().__init__(json)


class UsedCar(Car):
    def __init__(self, json):
        self.mileage = json["mileage"]
        self.ownerCount = json["ownerCount"]
        self.modifications = json["modifications"]
        super().__init__(json)

# %%
