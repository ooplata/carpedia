# Carpedia - Camilo Heras, Omar Plata
OOP Project 2022-1

## Getting Started
Code is located inside the src folder. To try out the program, run the `main.py` file.

## Functional requirements
-[x] The user may want to scroll through a comprehensive list of vehicles
-[x] The user may want to look at price graphs of certain vehicles

## Tasks
-[x] Prevent unexpected program closure
-[x] Show the user information on selected vehicles
-[x] Show the user a price graph on selected vehicles

## UML
![image](https://user-images.githubusercontent.com/99055524/164342897-e2366f3d-57c4-4869-a052-9a7e41fedf17.png)

```PUML
@startuml Project
class ImportedCar extends Car {
    -importedOn: DateTime
    -originalCountry: String
}

class UsedCar extends Car {
    -mileage: Float
    -modifications: List<String>
}

class NewCar extends Car {
    -concessionaire: String
}

class Car implements Internals {
    -releaseYear: DateTime
    -model: String
    -brand: String
    -body: String
    -priceHistory: Dictionary<DateTime,Float>
    -internals: Internals
}

class Internals implements Engine {
    -engine: Engine
    -transmission: String
    -4wb: bool
    -powerTrain: String
    -fuelType: FuelType
    -fuelConsumption: Float
}

enum FuelType {
    -Gasoline
    -Diesel
    -Premium
}

class Engine {
    -size: Float
    -cylinders: Int
    -inductionType: InductionType
    -horsePower: Int
    -torque: Int
}

enum InductionType {
    -Turbo
    -Super
}

class MotorUtility {
    -urls: List<String>
    -getLatestArticle() -> MotorArticle
    -getArticlesWithCar(Car) -> [MotorArticle]
    -openArticle(MotorArticle)
}

class MotorArticle {
    -publishDate: DateTime
    -body: String
    -getAllCars() -> [Car]
}

class WatchListItem implements Watchable {
    -model: String
    -oldPrice: Float
    -newPrice: Float
}

class Watchable {
    -hasChanges: Bool
    -acceptChanges()
    -getChanges()
}
@enduml
```
