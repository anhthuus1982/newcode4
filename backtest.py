# backtest.py
# File nay chay backtest cho chien luoc

class BacktestEngine:
    def __init__(self, strategy, historical_data):
        self.strategy = strategy
        self.historical_data = historical_data

    def run(self):
        """Chay backtest va tra ve danh sach tin hieu"""
        signals = []
        for i in range(len(self.historical_data)):
            window = self.historical_data[:i+1]
            signal = self.strategy.execute(window)
            signals.append(signal)
        return signals

# Vi du su dung
if __name__ == "__main__":
    historical_data = [100, 101, 102, 103, 104, 105]  # Du lieu gia vi du
    strategy = MACrossoverStrategy("strategies.json")
    backtest = BacktestEngine(strategy, historical_data)
    results = backtest.run()
    print("Ket qua backtest:", results)