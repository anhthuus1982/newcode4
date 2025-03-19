# config.py
# File nay chua cac thong tin cau hinh chung cho he thong

class Config:
    # API key va secret cho Bybit testnet
    API_KEY = "Sz22UaG1jqf308kkho"
    API_SECRET = "xRyGqc7LKBYm6KVzLSJkcZTnTV9pTV0LEUmb"
    
    # URL cua Bybit testnet
    BASE_URL = "https://api-testnet.bybit.com"
    
    # Cap giao dich mac dinh
    SYMBOL = "BTCUSDT"
    
    # Timeframe mac dinh
    TIMEFRAME = "1h"
    
    # Duong dan den database
    DB_PATH = "trading_data.db"
    
    # Token cho Telegram bot
    TELEGRAM_TOKEN = "8142778775:AAEb8h0cas4xxSUwcbcH_L_goUbyABgUI6E"
    
    # Chat ID cho Telegram
    TELEGRAM_CHAT_ID = "1401151166"
    
    # WebSocket URL cho Bybit testnet
    WS_URL = "wss://stream-testnet.bybit.com/v5/public/linear"