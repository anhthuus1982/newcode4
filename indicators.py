# indicators.py
# File nay tinh toan cac chi bao ky thuat

def calculate_moving_average(data, period):
    """Tinh moving average"""
    if len(data) < period:
        return None
    return sum(data[-period:]) / period

def calculate_rsi(data, period=14):
    """Tinh chi bao RSI"""
    if len(data) < period:
        return None
    gains = []
    losses = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        gains.append(diff if diff > 0 else 0)
        losses.append(-diff if diff < 0 else 0)
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))