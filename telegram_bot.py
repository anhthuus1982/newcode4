# telegram_bot.py
# File nay giao tiep voi Telegram API de dieu khien bot

import requests
from config import Config
from telegram.ext import Application, CommandHandler

class TelegramBot:
    def __init__(self):
        self.token = Config.TELEGRAM_TOKEN
        self.chat_id = Config.TELEGRAM_CHAT_ID
        # Su dung ApplicationBuilder thay vi Updater
        self.application = Application.builder().token(self.token).build()
        self.setup_handlers()

    def send_message(self, message):
        """Gui tin nhan den Telegram"""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            print("Gui tin nhan thanh cong")
        except requests.RequestException as e:
            print(f"Loi gui tin nhan Telegram: {e}")

    def start_command(self, update, context):
        """Xu ly lenh /start"""
        response = requests.post("http://localhost:5000/start")
        update.message.reply_text(response.json().get("message"))

    def stop_command(self, update, context):
        """Xu ly lenh /stop"""
        response = requests.post("http://localhost:5000/stop")
        update.message.reply_text(response.json().get("message"))

    def setup_handlers(self):
        """Cau hinh cac lenh Telegram"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("stop", self.stop_command))

    def run(self):
        """Khoi dong bot Telegram"""
        self.application.run_polling()

# Khoi tao instance
telegram_bot = TelegramBot()

if __name__ == "__main__":
    telegram_bot.run()