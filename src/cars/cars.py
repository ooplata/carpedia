from abc import ABC


# Definición de las clases
class Car(ABC):
    def __init__(self, releaseYear, model, brand, body, priceHistory,
    internals):
        self.releaseYear = releaseYear
        self.model = model
        self.brand = brand
        self.body = body
        self.priceHistory = priceHistory
        self.internals = internals

class ImportedCar(Car):
    def __init__(self, importedOn, originCountry, releaseYear, model, brand,
        body, priceHistory, internals):
        self.importedOn = importedOn
        self.originCountry = originCountry
        super().__init__(releaseYear, model, brand, body, priceHistory,
        internals)

class NewCar(Car):
    def __init__(self, dealership, releaseYear, model, brand, body,
    priceHistory, internals):
        self.dealership = dealership
        super().__init__(releaseYear, model, brand, body, priceHistory,
        internals)

class UsedCar(Car):
    def __init__(self, mileage, ownerCount, modifications, releaseYear, model,
    brand, body, priceHistory, internals):
        self.mileage = mileage
        self.ownerCount = ownerCount
        self.modifications = modifications
        super().__init__(releaseYear, model, brand, body, priceHistory,
        internals)
