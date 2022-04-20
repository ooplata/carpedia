from abc import ABC


class Car(ABC):
    ...

class ImportedCar(Car):
    pass

class NewCar(Car):
    pass

class UsedCar(Car):
    pass