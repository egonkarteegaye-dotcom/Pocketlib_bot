from flask import Flask
import threading
import asyncio
import random
import os
from datetime import datetime
from telegram import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return "GONKARTEE SON ROBOT IS LIVE"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask, daemon=True).start()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

SYMBOLS = ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD", "EUR/JPY", "GBP/JPY"]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            symbol = random.choice(SYMBOLS)
            signal = random.choice(["BUY 🟢", "SELL 🔴"])
            current_time = datetime.utcnow().strftime("%H:%M:%S UTC")
            message = f"🔥 GONKARTEE SON ROBOT 🔥\n\nPAIR: {symbol}\nSIGNAL: {signal}\nTIME: {current_time}\n\nTRADE NOW!"
            await bot.send_message(chat_id=CHANNEL_ID, text=message)
        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(120)

if __name__ == "__main__":
    asyncio.run(send_signal())
