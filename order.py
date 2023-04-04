from helpers import *

class Order:
    def __init__(self, order_type, side, price, qty):
        self.order_type = order_type
        self.side = side
        self.price = price
        self.qty = qty
    
    def __lt__(self, other):
        if not self.price:
            return True
        if self.side == Side.BUY:
            return self.price >= other.price
        else:
            return self.price <= other.price