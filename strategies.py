# strategies.py
# File nay dinh nghia cac chien luoc giao dich

import json
from indicators import calculate_moving_average

class Strategy:
    def __init__(self, config_file):
        """Khoi tao chien luoc voi file cau hinh"""
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def execute(self, market_data):
        """Thuc thi chien luoc - phuong thuc ao"""
        raise NotImplementedError("Phai trien khai execute trong lop con")

class MACrossoverStrategy(Strategy):
    def execute(self, market_data):
        """Chien luoc giao dich dua tren MA crossover"""
        short_period = self.config["params"]["short_period"]
        long_period = self.config["params"]["long_period"]
        short_ma = calculate_moving_average(market_data, short_period)
        long_ma = calculate_moving_average(market_data, long_period)
        if short_ma is None or long_ma is None:
            return "hold"
        if short_ma > long_ma:
            return "buy"
        elif short_ma < long_ma:
            return "sell"
        return "hold"