# websocket_client.py
# File nay quan ly ket noi WebSocket

import websocket
from config import Config

class WebSocketClient:
    def __init__(self):
        self.url = Config.WS_URL
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)

    def on_message(self, ws, message):
        """Xu ly du lieu nhan duoc"""
        print(f"Nhan du lieu: {message}")

    def on_error(self, ws, error):
        """Xu ly loi WebSocket"""
        print(f"Loi WebSocket: {error}")

    def on_close(self, ws, *args):
        """Xu ly khi dong ket noi"""
        print("Ket noi WebSocket da dong")

    def on_open(self, ws):
        """Xu ly khi mo ket noi"""
        print("Ket noi WebSocket thanh cong")
        ws.send('{"op": "subscribe", "args": ["tickers.BTCUSDT"]}')

    def connect(self):
        """Ket noi WebSocket"""
        self.ws.run_forever()

# Khoi tao instance
ws_client = WebSocketClient()