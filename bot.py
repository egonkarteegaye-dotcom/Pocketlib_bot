import asyncio
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@YOUR_CHANNEL_HERE"

START_TIMER = 2  # EXACTLY 2 MINUTES AHEAD
MIXED_LIMIT_MIN = 2
MIXED_LIMIT_MAX = 5
SIGNAL_INTERVAL = 60

bot = Bot(token=TELEGRAM_TOKEN)

async def main():
    print("Bot Started - Time 2 min Fixed + 90-92% Fixed!")
    while True:
        now = datetime.now(pytz.utc)
        # TIME FIX: NOW + 2 MINUTES EXACTLY
        entry_time_obj = now + timedelta(minutes=2)
        signal_time = now.strftime('%H:%M:%S')
        entry_time = entry_time_obj.strftime('%H:%M:%S')
        
        pair = random.choice(["EUR/GBP (OTC)","EUR/USD (OTC)","GBP/USD (OTC)","AUD/JPY (OTC)","USD/JPY (OTC)"])
        direction = random.choice(["BUY 🟢 UP", "SELL 🔴 DOWN"])
        accuracy = random.randint(90, 92)  # FORCE 90-92%
        expiry = random.randint(2, 5)  # MIXED 2-5 MIN
        rsi = random.randint(20, 80)

        signal = f"""🔥 POCKET OPTION PREDICTION 🔥

📩 SIGNAL RECEIVED: {signal_time} UTC
💰 PAIR: {pair}
📊 PREDICTION: {direction}
📈 RSI: {rsi}
🎯 ACCURACY: {accuracy}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {entry_time} UTC ( +2 MIN )
⏱️ EXPIRY: {expiry} MINUTES (Mixed 2-5)

⚡ SET UP NOW:
1. Open {pair}
2. Set expiry {expiry} min
3. WAIT for {entry_time}

⚡ AT {entry_time} EXACTLY → CLICK {direction}!

━━━━━━━━━━━━━━
GOLD ELITE VIP 🔥"""

        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=signal)
            print(f"Sent: Signal {signal_time} -> Entry {entry_time} (+2 min) | {accuracy}%")
        except Exception as e:
            print(e)
        await asyncio.sleep(SIGNAL_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
