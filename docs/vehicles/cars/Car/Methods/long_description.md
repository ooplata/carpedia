# Car.long_description Method
Gets a string representation of this car's full property set.

```Python
@abstractmethod
def long_description(self) -> str
```

## Remarks
This method is mostly used in GUI scenarios. It is recommended to override it in derived classes, as you may end up with an incomplete description otherwise.