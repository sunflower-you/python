from enum import Enum, IntEnum, unique
from icecream import ic


class QuantType(Enum):
    SymQuant = 0
    AsymQuant = 1


ic(QuantType.SymQuant, QuantType.SymQuant.name, QuantType.SymQuant.value)
ic(type(QuantType.SymQuant.value))
ic(type(QuantType.SymQuant))


class QuantType3(IntEnum):
    SymQuant = 0
    AsymQuant = 1


ic(QuantType3.SymQuant, QuantType3.SymQuant.name, QuantType3.SymQuant.value)
ic(type(QuantType3.SymQuant.value))
ic(type(QuantType3.SymQuant))


class QuantType0(Enum):
    SymQuant = "SymQuant"
    AsymQuant = "AsymQuant"


ic(QuantType0.SymQuant, QuantType0.SymQuant.name, QuantType0.SymQuant.value)
ic(type(QuantType0.SymQuant.value))
ic(type(QuantType0.SymQuant))


class QuantType2(str, Enum):
    SymQuant = "SymQuant"
    AsymQuant = "AsymQuant"


ic(QuantType2.SymQuant, QuantType2.SymQuant.name, QuantType2.SymQuant.value)
ic(type(QuantType2.SymQuant.value))
ic(type(QuantType2.SymQuant))



@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'


print(Month.Jan, '----------',Month.Jan.name, '----------', Month.Jan.value)
for name, member in Month.__members__.items():
    print(name, '----------', member, '----------', member.value)