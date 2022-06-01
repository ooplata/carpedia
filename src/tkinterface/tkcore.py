# %%
from abc import ABC, abstractmethod

import tkinter as tk


# %%
class Application(ABC):
    def __init__(self, title: str, iconPath: str,
                 geometry: str) -> None:
        self.window = tk.Tk()
        self.window.title(title)
        self.window.iconbitmap(iconPath)
        self.window.geometry(geometry)

    def run(self):
        self.window.update()

        self.onstartup()
        self.window.mainloop()
        self.onclosure()

    @abstractmethod
    def onstartup(self):
        ...

    @abstractmethod
    def onclosure(self):
        ...

# %%
