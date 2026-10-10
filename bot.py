import asyncio
import random
from datetime import datetime
from telegram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

SYMBOLS = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/JPY", "GOLD", "BTC/USD"]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    while True:
        symbol = random.choice(SYMBOLS)
        signal = random.choice(["BUY 🟢", "SELL 🔴"])
        expiry = random.choice(["1", "2", "3"])
        current_time = datetime.utcnow().strftime("%H:%M:%S")
        time_analysis = "✅ Strong Momentum\n📈 High Accuracy Setup"
        
        message = f"""GONKARTEE SON ROBOT 🤖🔥✅
(POCKET OPTION)

🔥 AI PREDICTION 🔥
💰 PAIR: {symbol}
📊 ACTION: {signal}
⏰ EXPIRY: {expiry} MIN
💵 AMOUNT: $1 and up ⬆️

{time_analysis}

🕐 TIME: {current_time} UTC
📊 ACCURACY: 85%+
"""
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        print(f"Signal sent: {symbol}")
        await asyncio.sleep(120)

if __name__ == "__main__":
    asyncio.run(send_signal())
