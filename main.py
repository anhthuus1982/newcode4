# main.py
# File nay chay toan bo he thong, bao gom bot, giao dien web va API dieu khien

from exchange import exchange
from database import db_manager
from telegram_bot import telegram_bot
from websocket_client import ws_client
import threading
import logging
from flask import Flask, jsonify, render_template  # Thêm render_template vào import

app = Flask(__name__, template_folder="templates", static_folder="static")
bot_running = False  # Trang thai bot: True = dang chay, False = dung
ws_thread = None

# Cau hinh logging
logging.basicConfig(filename="bot.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

def run_websocket():
    """Chay WebSocket trong thread rieng"""
    if bot_running:
        ws_client.connect()

def start_bot():
    """Khoi dong bot"""
    global bot_running, ws_thread
    if not bot_running:
        bot_running = True
        logging.info("Bot da khoi dong")
        ws_thread = threading.Thread(target=run_websocket)
        ws_thread.start()
        telegram_bot.send_message("Bot da khoi dong!")
        return True
    return False

def stop_bot():
    """Dung bot"""
    global bot_running, ws_thread
    if bot_running:
        bot_running = False
        ws_client.ws.close()  # Dong ket noi WebSocket
        logging.info("Bot da dung")
        telegram_bot.send_message("Bot da dung!")
        if ws_thread:
            ws_thread.join()  # Doi thread ket thuc
        return True
    return False

@app.route("/")
def index():
    """Hien thi giao dien web"""
    with open("bot.log", "r") as f:
        logs = f.readlines()
    return render_template("index.html", status="Running" if bot_running else "Stopped", logs=logs)  # Sửa app.render_template thành render_template

@app.route("/start", methods=["POST"])
def api_start():
    """API de khoi dong bot"""
    if start_bot():
        return jsonify({"message": "Bot started"}), 200
    return jsonify({"message": "Bot already running"}), 400

@app.route("/stop", methods=["POST"])
def api_stop():
    """API de dung bot"""
    if stop_bot():
        return jsonify({"message": "Bot stopped"}), 200
    return jsonify({"message": "Bot already stopped"}), 400

if __name__ == "__main__":
    # Ket noi database va tao bang
    db_manager.connect()
    db_manager.create_table()

    # Lay du lieu thi truong
    market_data = exchange.get_market_data()
    logging.info(f"Du lieu thi truong: {market_data}")

    # Khoi dong Flask server
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)