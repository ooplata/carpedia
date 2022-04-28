# %%
from abc import ABC
from cars.internals import Internals


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


class ImportedCar(Car):
    def __init__(self, json):
        self.importedOn = json["importedOn"]
        self.originCountry = json["originalCountry"]
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
