from abc import ABC
import internals

#Definición de las clases
class Car(ABC):
    def __init__(self, releaseYear, model, brand, body, priceHistory, internals):
        self.releaseYear = releaseYear
        self.model = model
        self.brand = brand
        self.body = body
        self.priceHistory = priceHistory
        self.internals = Internals

class ImportedCar(Car):
    def __init__(self, importedOn, originCountry):
        self.importedOn = importedOn
        self.originCountry = originCountry

class NewCar(Car):
    def __init__(self, dealership):
        self.dealership = dealership

class UsedCar(Car):
    def __init__(self, mileage, ownerCount, modifications):
        self.mileage = mileage
        self.ownerCount = ownerCount
        self.modifications = modifications