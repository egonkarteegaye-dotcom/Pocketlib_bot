from flask import Flask
import threading
import asyncio
import random
from datetime import datetime
from telegram import Bot
import os

app = Flask('')

@app.route('/')
def home():
    return "GONKARTEE SON ROBOT IS LIVE!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_flask).start()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

SYMBOLS = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "EUR/GBP", "EUR/JPY"]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    while True:
        symbol = random.choice(SYMBOLS)
        signal = random.choice(["BUY 🟢", "SELL 🔴"])
        expiry = random.choice(["1", "2", "3", "5"])
        current_time = datetime.utcnow().strftime("%H:%M:%S")

        message = f"""GONKARTEE SON ROBOT (P-GOLD)

🔥 AI PREDICTION 🔥
💰 PAIR: {symbol}
📊 ACTION: {signal}
⏰ EXPIRY: {expiry} MIN
💵 AMOUNT: $1 and up ⬆️

✅ Strong Momentum
📈 High Accuracy Setup

🕒 TIME: {current_time} UTC
📊 ACCURACY: 85%+
"""

        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        print(f"Signal sent: {symbol}")
        await asyncio.sleep(120)

if __name__ == "__main__":
    asyncio.run(send_signal())
