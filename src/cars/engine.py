# %%
# Definición de la clase
class Engine:
    def __init__(self, json):
        self.size = json["size"]
        self.cylinders = json["cylinders"]
        self.inductionType = json["inductionType"]
        self.horsePower = json["horsePower"]
        self.torque = json["torque"]

# %%
