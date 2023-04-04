from heapq import heappush, heappop
from helpers import *
from order import Order

class MatchingEngine:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
    
    def add_order(self, order):
        if order.order_type == OrderType.MARKET:
            self.match_market_order(order)
            return 
        if order.side == Side.BUY:
            heappush(self.buy_orders, order)
        else:
            heappush(self.sell_orders, order)
        self.match_orders()
    
    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy_order = self.buy_orders[0]
            best_sell_order = self.sell_orders[0]
            if best_buy_order.order_type == OrderType.LIMIT and best_sell_order.order_type == OrderType.LIMIT and best_buy_order.price < best_sell_order.price:
                break
            if best_buy_order.qty == best_sell_order.qty:
                trade_qty = best_buy_order.qty
                trade_price = best_buy_order.price
                heappop(self.buy_orders)
                heappop(self.sell_orders)
            elif best_buy_order.qty > best_sell_order.qty:
                trade_qty = best_sell_order.qty
                trade_price = best_sell_order.price
                if not trade_price:
                    trade_price = best_buy_order.price
                best_buy_order.qty -= best_sell_order.qty
                heappop(self.sell_orders)
            else:
                trade_qty = best_buy_order.qty
                trade_price = best_buy_order.price
                if not trade_price:
                    trade_price = best_sell_order.price
                best_sell_order.qty -= best_buy_order.qty
                heappop(self.buy_orders)
            print(f"Trade, price: {trade_price}, qty: {trade_qty}")
    
    def match_market_order(self, market_order):
        if market_order.side == Side.BUY:
            while self.sell_orders and market_order.qty > 0:
                best_sell_order = self.sell_orders[0]
                if market_order.qty >= best_sell_order.qty:
                    trade_qty = best_sell_order.qty
                    trade_price = best_sell_order.price
                    market_order.qty -= best_sell_order.qty
                    heappop(self.sell_orders)
                else:
                    trade_qty = market_order.qty
                    trade_price = best_sell_order.price
                    best_sell_order.qty -= market_order.qty
                    market_order.qty = 0
                print(f"Trade, price: {trade_price}, qty: {trade_qty}")
            if market_order.qty > 0:
                print("Market order not fully executed, removing order...")
        else:
            while self.buy_orders and market_order.qty > 0:
                best_buy_order = self.buy_orders[0]
                if market_order.qty >= best_buy_order.qty:
                    trade_qty = best_buy_order.qty
                    trade_price = best_buy_order.price
                    market_order.qty -= best_buy_order.qty
                    heappop(self.buy_orders)
                else:
                    trade_qty = market_order.qty
                    trade_price = best_buy_order.price
                    best_buy_order.qty -= market_order.qty
                    market_order.qty = 0
                print(f"Trade, price: {trade_price}, qty: {trade_qty}")
            if market_order.qty > 0:
                print("Market order not fully executed, removing order...")
    
    def process_input(self, input_string):
        parts = input_string.split()
        order_type = OrderType[parts[0].upper()]
        side = Side[parts[1].upper()]
        if order_type == OrderType.LIMIT:
            price = float(parts[2])
            qty = int(parts[3])
        else:
            price = None
            qty = int(parts[2])
        self.add_order(Order(order_type, side, price, qty))