from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

import bot.logging_config


print("\n===== BINANCE FUTURES TRADING BOT =====\n")

symbol = input("Enter Symbol (example BTCUSDT): ").upper()

side = input("Enter Side (BUY/SELL): ").upper()

if not validate_side(side):
    print("Invalid Side")
    exit()


order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()

if not validate_order_type(order_type):
    print("Invalid Order Type")
    exit()


quantity = input("Enter Quantity: ")

if not validate_quantity(quantity):
    print("Invalid Quantity")
    exit()


if order_type == "MARKET":

    result = place_market_order(
        symbol,
        side,
        quantity
    )

else:

    price = input("Enter Price: ")

    result = place_limit_order(
        symbol,
        side,
        quantity,
        price
    )


print("\n===== ORDER RESPONSE =====\n")

if isinstance(result, dict):

    print("Order ID:", result.get("orderId"))
    print("Symbol:", result.get("symbol"))
    print("Status:", result.get("status"))
    print("Side:", result.get("side"))
    print("Type:", result.get("type"))

else:

    print("ERROR:", result)