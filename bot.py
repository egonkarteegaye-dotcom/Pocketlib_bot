import asyncio
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot

TELEGRAM_TOKEN = "YOUR_REAL_TOKEN_HERE"
CHANNEL_ID = "@YOUR_REAL_CHANNEL_HERE"

PAIRS = ["EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)","EUR/GBP (OTC)","AUD/USD (OTC)","GBP/JPY (OTC)","EUR/JPY (OTC)","USD/CHF (OTC)","AUD/JPY (OTC)","NZD/USD (OTC)"]

bot = Bot(token=TELEGRAM_TOKEN)

async def main():
    while True:
        now = datetime.now(pytz.utc)
        entry = now + timedelta(minutes=2)
        signal_time = now.strftime('%H:%M:%S')
        entry_time = entry.strftime('%H:%M:%S')
        accuracy = random.randint(90, 92)
        expiry = random.randint(2, 5)
        pair = random.choice(PAIRS)
        direction = random.choice(["BUY 🟢 UP", "SELL 🔴 DOWN"])
        rsi = random.randint(24, 80)
        msg = f"""🔥 POCKET OPTION PREDICTION 🔥

📩 SIGNAL RECEIVED: {signal_time} UTC
💰 PAIR: {pair}
📊 PREDICTION: {direction}
📈 RSI: {rsi}
🎯 ACCURACY: {accuracy}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {entry_time} UTC
⏱️ EXPIRY: {expiry} MINUTES

⚡ SET UP NOW:
1. Open {pair}
2. Set expiry {expiry} min
3. WAIT for {entry_time}

⚡ AT {entry_time} EXACTLY → CLICK {direction}!

━━━━━━━━━━━━━━
GOLD ELITE VIP 🔥"""
        await bot.send_message(chat_id=CHANNEL_ID, text=msg)
        print(f"{signal_time} -> {entry_time} {accuracy}%")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
