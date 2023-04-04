# Matching Engine

A simple matching engine developed to quickly and fairly match orders in an exchange, following these premises:

- The engine handles only 1 asset
- The possible order types are limit (a passive order at a fixed price) and market (an order to be filled at the best available price immediately)
- It's not necessary to save the orders and trades, all the information can be kept on volatile memory
- It's not necessary to think about hardware scalability and cloud/elasticity tools, such as Kubernetes

The Matching Engine takes orders with the following information:

- Type (limit/market)
- Side (buy/sell)
- Price (for limit orders)
- Qty

Limit orders with prices that would trigger a trade can be ignored or filled, however, the chosen behavior must be justified.

When a trade is done, the following should be output: "Trade, price: <trade price>, qty: <shares>"

## Bonus Points

- Solutions capable of matching a market order with complexity O(log n), being 'n' the number of open orders.
- Solutions that take into account the arrival order of orders. In the previous example, this would mean that the first sell order with qty=100 should be filled before the second, with qty=200.

## Usage

To use the Matching Engine, follow these steps:

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Import the `MatchingEngine` class from `matchingEngine.py`.
4. Create an instance of the `MatchingEngine` class.
5. Add orders to the Matching Engine with the `add_order()` method.
6. Trades will be automatically executed and printed to the console when orders are matched.

## Examples

```python
from matchingEngine import MatchingEngine, OrderType, Side, Order

# Create a Matching Engine instance
engine = MatchingEngine()

# Add limit buy order
buy_order = Order(OrderType.LIMIT, Side.BUY, 10, 100)
engine.add_order(buy_order)

# Add limit sell orders
sell_order1 = Order(OrderType.LIMIT, Side.SELL, 20, 100)
sell_order2 = Order(OrderType.LIMIT, Side.SELL, 20, 200)
engine.add_order(sell_order1)
engine.add_order(sell_order2)

# Add market buy order
market_buy_order = Order(OrderType.MARKET, Side.BUY, None, 150)
engine.add_order(market_buy_order)

# Output: "Trade, price: 20, qty: 150"
