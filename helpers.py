from enum import Enum

class OrderType(Enum):
    LIMIT = 1
    MARKET = 2

class Side(Enum):
    BUY = 1
    SELL = 2