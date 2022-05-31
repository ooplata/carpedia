# Car.short_description Method
Gets a short summary of this car's properties in string form.

```Python
@abstractmethod
def short_description(self) -> str
```

## Remarks
This method is mostly used in GUI scenarios. It is not very useful to override it in derived classes, due to the fact that this is a short description string. However, the method is still marked as abstract to account for every possible scenario. If you don't want to override it, use `super()` to return the result of this method within its base class.