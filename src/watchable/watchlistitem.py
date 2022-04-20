from watchable import Watchable


class WatchListItem(Watchable):
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def oldPrice(self):
        return self._oldPrice

    @oldPrice.setter
    def oldPrice(self, value):
        self._oldPrice = value

    @property
    def newPrice(self):
        return self._newPrice

    @newPrice.setter
    def newPrice(self, value):
        self._oldPrice = value