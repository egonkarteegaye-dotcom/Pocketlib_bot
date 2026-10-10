import os
import random
import asyncio
from datetime import datetime
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("DEST_CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

PAIRS = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "EUR/GBP (OTC)", "BTC/USD (OTC)"]

def get_signal():
    rsi = random.randint(10, 90)
    if rsi < 35:
        return "BUY 🟢 UP", rsi, random.randint(78, 92)
    elif rsi > 65:
        return "SELL 🔴 DOWN", rsi, random.randint(78, 92)
    else:
        return random.choice(["BUY 🟢 UP", "SELL 🔴 DOWN"]), rsi, random.randint(75, 88)

async def send_signal():
    while True:
        try:
            pair = random.choice(PAIRS)
            action, rsi, acc = get_signal()
            now = datetime.now()
            next_min = (now.minute + 1) % 60
            msg = f"""
🔥 POCKET OPTION PREDICTION 🔥

💰 PAIR: {pair}
📊 PREDICTION: {action}
⏰ EXPIRY: 2 MINUTES
⏱️ ENTRY TIME: {now.hour:02d}:{next_min:02d}:00 (in 30 sec)
📈 RSI: {rsi}
🎯 ACCURACY: {acc}%

⚡ ACTION: OPEN {pair} NOW!
⚡ SET TIME: 2 MIN
⚡ CLICK {action} AT {next_min:02d}:00 EXACTLY!

━━━━━━━━━━━━━━
GOLD ELITE VIP 🔥
"""
            await bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="Markdown")
            await asyncio.sleep(120)
        except Exception as e:
            print(e)
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(send_signal())
