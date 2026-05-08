from binance.client import Client

API_KEY = "HIQsGRqgCV2zh1wWklAt8Goe7BFYzeUT6ghAOtpzGB0WrPta3iLiVUt16E8ykpBg"
API_SECRET = "J7t05DkpbEvMFNiroLwJ3S27jw1boBpbB3LEKkyd0PefEm83s475CyiacWmNDjGI"

client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client