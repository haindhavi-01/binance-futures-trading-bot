from bot.client import get_client
import logging

client = get_client()

def place_market_order(symbol, side, quantity):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"MARKET ORDER SUCCESS: {order}")

        return order

    except Exception as e:

        logging.error(f"MARKET ORDER FAILED: {e}")

        return str(e)


def place_limit_order(symbol, side, quantity, price):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"LIMIT ORDER SUCCESS: {order}")

        return order

    except Exception as e:

        logging.error(f"LIMIT ORDER FAILED: {e}")

        return str(e)