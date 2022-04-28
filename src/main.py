from cars.cars import ImportedCar
from cars.engine import Engine
from cars.internals import Internals


carEngine = Engine(4 , 4 , "Super" , 2 , "Torque")

carInternals = Internals(carEngine , "Manual" , "Open" , "Front" ,
"Gasoline" , 6.5)

car = ImportedCar(2022 , "USA" , 2022 , "Mito" , "AlfaRomeo" , "Compact"
, 0, carInternals)

val = input("What would you like to see in an imported car?\n")
print(F"Check out this amazing imported car!\n\n{car.model} from {car.brand} " +
F"({car.releaseYear})\nImported in {car.importedOn} from {car.originCountry}")
