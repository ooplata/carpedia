# Carpedia - Camilo Heras, Omar Plata
OOP Project 2022-1  

Functional requirement: The user may want to customize their preferences when it comes to aspects such as bodystyle/make/age.  

Task 1; the program does not close unexpectedly and shows the user information on a vehicle

## Getting Started
Code is located inside the src folder. To try out the program, run the `main.py` file.

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
