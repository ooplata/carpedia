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
| [Application(str, str, str)](Application/init.md) | Initializes a new instance of the Application class with the specified options. |

## Properties
| | |
| --------------- | --------------- |
| [window](Application/window.md) | A simple Tkinter window. |

## Methods
| | |
| --------------- | --------------- |
| [run()](Application/run.md) | Starts the app. |
| [onstartup()](Application/onstartup.md) | Invoked when the app is started. Override this method to initialize your app. |
| [onexit()](Application/onexit.md) | Invoked when the main window's main loop is done executing. Override this method to perform any necessary cleanup or save user progress before the app is closed. |