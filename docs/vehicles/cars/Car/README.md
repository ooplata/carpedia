# Car
The base car class to derive custom cars from.

```Python
class Car(ABC)
```

## Constructors
| | |
| --------------- | --------------- |
| [Car(json)](Constructors/init.md) | Initializes a new instance of the Car class with data from the specified JSON. |

## Properties
| | |
| --------------- | --------------- |
| [body](Properties/body.md) | The body type for this car. |
| [brand](Properties/brand.md) | The brand this car belongs to. |
| [internals](Properties/internals.md) | Represents this car's internal components. |
| [model](Properties/model.md) | Model name for this car. |
| [priceHistory](Properties/priceHistory.md) | Contains the retail prices for this car across multiple years. |
| [releaseYear](Properties/releaseYear.md) | The year this car was released in. |

## Methods
| | |
| --------------- | --------------- |
| [long_description()](Methods/long_description.md) | Gets a string representation of this car's full property set. |
| [short_description()](Methods/short_description.md) | Gets a short summary of this car's properties in string form. |