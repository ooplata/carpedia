# Engine(json) Constructor
Initializes a new instance of the Engine class with data from the specified JSON.

```Python
def __init__(self, json) -> None
```

## Parameters
### `json` json
Data for the Engine in JSON format. Your JSON should look roughly like the following:

```JSON
{
	"size": 1.4,
	"cylinders": 4,
	"inductionType": "Turbocharged",
	"horsePower": 155,
	"torque": 230
}
```

## Remarks
If you want to create a class that inherits this one, add data to the JSON accordingly and update the constructor. You can then call this class' constructor through `super()`.