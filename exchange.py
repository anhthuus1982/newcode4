# exchange.py
# File nay tuong tac voi API cua Bybit

import requests
import hmac
import hashlib
import time
from config import Config

class BybitExchange:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.api_secret = Config.API_SECRET
        self.base_url = Config.BASE_URL

    def _generate_signature(self, params):
        """Tao chu ky cho yeu cau API"""
        param_str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
        return hmac.new(
            self.api_secret.encode("utf-8"),
            param_str.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def get_market_data(self, symbol=Config.SYMBOL):
        """Lay du lieu thi truong cho cap giao dich"""
        endpoint = f"{self.base_url}/v5/market/tickers?category=linear&symbol={symbol}"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Loi lay du lieu thi truong: {e}")
            return None

    def place_order(self, symbol, side, quantity, price):
        """Dat lenh giao dich"""
        endpoint = f"{self.base_url}/v5/private/order/create"
        params = {
            "api_key": self.api_key,
            "symbol": symbol,
            "side": side,
            "order_type": "Limit",
            "qty": quantity,
            "price": price,
            "time_in_force": "GoodTillCancel",
            "timestamp": int(time.time() * 1000)
        }
        params["sign"] = self._generate_signature(params)
        try:
            response = requests.post(endpoint, json=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Loi dat lenh: {e}")
            return None

# Khoi tao instance
exchange = BybitExchange()