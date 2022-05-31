# Application.run Method
Starts the app.

```Python
def run()
```

## Remarks
This method will keep running until the Application is closed, so make sure to run this only after fully setting up your entry point. This shouldn't be a problem as long as you use the [onstartup](onstartup.md) method to run initialization code.