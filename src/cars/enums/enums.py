from enum import Enum


class FuelType(Enum):
    gasoline = 0,
    diesel = 1,
    premium = 2

class InductionType(Enum):
    turbo = 0,
    super = 1