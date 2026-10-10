import asyncio, random, threading, os
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from flask import Flask

# --- YOUR SETTINGS ---
TOKEN = os.environ.get("TELEGRAM_TOKEN", "8434602399:AAH-6K4m3K5a5a5a_REPLACE_WITH_YOUR_TOKEN")
CHANNEL = os.environ.get("CHANNEL_ID", "@REPLACE_WITH_YOUR_CHANNEL")

bot = Bot(token=TOKEN)

# Fix Render No open ports
app = Flask(__name__)
@app.route('/')
def home(): return "GOLD ELITE 90-95% LIVE"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
threading.Thread(target=run_web, daemon=True).start()

PAIRS = ["EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)","EUR/GBP (OTC)","AUD/USD (OTC)","EUR/JPY (OTC)","GBP/JPY (OTC)","USD/CAD (OTC)"]

async def main():
    print("GOLD ELITE 90-95% STARTED")
    while True:
        try:
            now = datetime.now(pytz.utc)
            entry = now + timedelta(minutes=2)  # 2 MINUTES BEFORE LOGIC
            
            # ALL VERSION WITH SECONDS
            st = now.strftime('%H:%M:%S')
            et = entry.strftime('%H:%M:%S')
            
            # ACCURACY 90-95% (or 92 as you asked)
            acc = random.randint(90, 95)  # Will give 90,91,92,93,94,95%
            
            pair = random.choice(PAIRS)
            pred = random.choice(['BUY 🟢 UP ⬆️','SELL 🔴 DOWN ⬇️'])
            direction = "UP" if "BUY" in pred else "DOWN"

            # GOLD ELITE ALL VERSION FORMAT
            msg = f"""🔥 POCKET OPTION GOLD ELITE VIP 🔥

📩 SIGNAL RECEIVED: {st} UTC
💰 PAIR: {pair}
📈 DIRECTION: {direction}
📊 PREDICTION: {pred}
🎯 ACCURACY: {acc}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {et} UTC
⏱️ EXPIRY: 3 MIN
━━━━━━━━━━━━━━

⚡ 2 MINUTES PREPARATION!
⚡ AT {et} EXACTLY CLICK {direction}!

🔥 GOLD ELITE {acc}% VIP 🔥"""

            await bot.send_message(chat_id=CHANNEL, text=msg)
            print(f"GOLD SENT: Received {st} -> Entry {et} | {pair} {pred} {acc}%")
            
        except Exception as e:
            print(f"ERROR: {e}")
        
        await asyncio.sleep(60)  # New signal every 1 minute

if __name__ == "__main__":
    asyncio.run(main())
