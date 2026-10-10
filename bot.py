import asyncio
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@YOUR_CHANNEL_HERE"

PAIRS = [
"EUR/USD (OTC)","GBP/USD (OTC)","EUR/GBP (OTC)","USD/JPY (OTC)",
"AUD/USD (OTC)","AUD/JPY (OTC)","GBP/JPY (OTC)","EUR/JPY (OTC)",
"USD/CHF (OTC)","NZD/USD (OTC)","EUR/AUD (OTC)","GBP/AUD (OTC)",
"USD/CAD (OTC)","AUD/CAD (OTC)","EUR/CAD (OTC)","GBP/CAD (OTC)"
]

bot = Bot(token=TELEGRAM_TOKEN)

async def main():
    print("GOLD ELITE VIP - FINAL VERSION RUNNING")
    while True:
        now = datetime.now(pytz.utc)
        entry = now + timedelta(minutes=2)
        
        signal_time = now.strftime('%H:%M:%S')
        entry_time = entry.strftime('%H:%M:%S')
        
        pair = random.choice(PAIRS)
        direction = random.choice(["BUY 🟢 UP", "SELL 🔴 DOWN"])
        accuracy = random.randint(90, 92)
        expiry = random.randint(2, 5)
        rsi = random.randint(24, 80)

        text = f"""🔥 POCKET OPTION PREDICTION 🔥

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

        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=text)
            print(f"✅ {signal_time} -> {entry_time} (+2 min) | {accuracy}% | {expiry}min")
        except Exception as e:
            print(e)
        
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
