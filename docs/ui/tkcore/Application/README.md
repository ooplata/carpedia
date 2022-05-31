# Application
The Application class encapsulates an app with a window-driven GUI.

```Python
class Application(ABC)
```

## Remarks
This class isn't very useful on its own. You may build your own app by creating a derived class from this one.

## Constructors
| | |
| --------------- | --------------- |
| [Application(str, str, str)](Constructors/init.md) | Initializes a new instance of the Application class with the specified options. |

## Properties
| | |
| --------------- | --------------- |
| [window](Properties/window.md) | An instance of the Tk class. |

## Methods
| | |
| --------------- | --------------- |
| [run()](Methods/run.md) | Starts the app. |
| [onstartup()](Methods/onstartup.md) | Invoked when the app is started. Override this method to initialize your app. |
| [onexit()](Methods/onexit.md) | Invoked when the main window's main loop is done executing. Override this method to perform any necessary cleanup or save user progress before the script is done running. |