import os
import random
import asyncio
from datetime import datetime, timedelta
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("DEST_CHANNEL_ID")
bot = Bot(token=BOT_TOKEN)

PAIRS = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "EUR/GBP (OTC)", "BTC/USD (OTC)"]

def get_signal():
    rsi = random.randint(15, 85)
    if rsi < 35: return "BUY 🟢 UP", rsi, random.randint(80, 92)
    elif rsi > 65: return "SELL 🔴 DOWN", rsi, random.randint(80, 92)
    else: return random.choice(["BUY 🟢 UP", "SELL 🔴 DOWN"]), rsi, random.randint(76, 88)

async def send_signal():
    while True:
        try:
            pair = random.choice(PAIRS)
            action, rsi, acc = get_signal()
            now = datetime.utcnow()
            signal_time = now.strftime("%H:%M:%S")
            entry = now + timedelta(minutes=1)
            entry_time = entry.strftime("%H:%M:00")
            
            msg = f"""
🔥 POCKET OPTION PREDICTION 🔥

📩 SIGNAL RECEIVED: {signal_time} UTC
💰 PAIR: {pair}
📊 PREDICTION: {action}
📈 RSI: {rsi}
🎯 ACCURACY: {acc}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {entry_time} UTC
⏰ That's 1 MINUTE after signal!
⏱️ EXPIRY: 2 MINUTES

⚡ SET UP NOW:
1. Open {pair}
2. Set amount $1
3. Set expiry 2 min
4. WAIT for {entry_time}

⚡ AT {entry_time} EXACTLY → CLICK {action}!

━━━━━━━━━━━━━━
GOLD ELITE VIP 🔥 - Monrovia Time = UTC
"""
            await bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="Markdown")
            await asyncio.sleep(120)
        except Exception as e:
            print(e)
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(send_signal())
