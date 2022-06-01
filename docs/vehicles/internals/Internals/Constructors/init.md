# Internals(json) Constructor
Initializes a new instance of the Internals class with data from the specified JSON.

```Python
def __init__(self, json) -> None
```

## Parameters
### `json` json
Data for the Internals in JSON format. Your JSON should look roughly like the following:

```JSON
{
	"engine": {
		"size": 1.4,
		"cylinders": 4,
		"inductionType": "Turbocharged",
		"horsePower": 155,
		"torque": 230
	},
	"transmission": "Manual",
	"4WD": false,
	"powerTrain": "Front",
	"fuelType": "Gasoline",
	"fuelConsumption": 6.5
}
```

## Remarks
If you want to create a class that inherits this one, add data to the JSON accordingly and update the constructor. You can then call this class' constructor through `super()`.