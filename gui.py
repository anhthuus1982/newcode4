# gui.py
# File nay cung cap giao dien nguoi dung

import tkinter as tk

class TradingView:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller
        self.root.title("Trading Bot")
        self.label = tk.Label(self.root, text="Welcome to Trading Bot")
        self.label.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.controller.start)
        self.start_button.pack()
        self.root.mainloop()

class TradingController:
    def __init__(self, exchange):
        self.exchange = exchange
        self.view = TradingView(self)

    def start(self):
        """Bat dau bot giao dich"""
        data = self.exchange.get_market_data()
        self.view.label.config(text=f"Market Data: {data}")

# Khoi tao
controller = TradingController(exchange)