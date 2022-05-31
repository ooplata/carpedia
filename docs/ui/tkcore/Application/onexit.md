# Application.onexit Method
Invoked when the main window's main loop is done executing. Override this method to perform any necessary cleanup or save user progress before the script is done running.

```Python
@abstractmethod
def onexit(self)
```

## Remarks
This method will run after the Application is closed, and the UI does not exist anymore by then. As a result, you have no access to any UI elements at this point, so consider them gone.