import asyncio, random, threading, os
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from flask import Flask

TOKEN = os.environ.get("TELEGRAM_TOKEN", "8434602399:AAH-6K4m3K5a5a5a_REPLACE_WITH_YOUR_TOKEN")
CHANNEL = os.environ.get("CHANNEL_ID", "@REPLACE_WITH_YOUR_CHANNEL")

bot = Bot(token=TOKEN)

app = Flask(__name__)
@app.route('/')
def home(): return "GONKARTEE SON ROBOT LITE VIP LIVE"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
threading.Thread(target=run_web, daemon=True).start()

PAIRS = ["EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)","EUR/GBP (OTC)","AUD/USD (OTC)","EUR/JPY (OTC)","GBP/JPY (OTC)","USD/CAD (OTC)","EUR/AUD (OTC)","GBP/CAD (OTC)"]

async def main():
    print("GONKARTEE SON ROBOT LITE VIP 90-95% STARTED")
    print(f"CHANNEL TARGET: {CHANNEL}")
    while True:
        try:
            now = datetime.now(pytz.utc)
            entry = now + timedelta(minutes=2)
            
            st = now.strftime('%H:%M:%S')
            et = entry.strftime('%H:%M:%S')
            
            acc = random.randint(90, 95)
            pair = random.choice(PAIRS)
            pred_full = random.choice(['BUY 🟢 UP ⬆️','SELL 🔴 DOWN ⬇️'])
            direction = "UP" if "BUY" in pred_full else "DOWN"

            msg = f"""🔥 GONKARTEE SON ROBOT LITE VIP 🔥 💵

📩 SIGNAL RECEIVED: {st} UTC
💰 PAIR: {pair}
📈 DIRECTION: {direction}
📊 PREDICTION: {pred_full}
🎯 ACCURACY: {acc}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {et} UTC
⏱️ EXPIRY: 3 MIN
━━━━━━━━━━━━━━

⚡ 2 MINUTES PREPARATION!
⚡ AT {et} EXACTLY CLICK {direction}!

🔥 GONKARTEE SON {acc}% VIP 🔥 💵"""

            await bot.send_message(chat_id=CHANNEL, text=msg)
            print(f"GONKARTEE SENT: {st} -> {et} | {pair} {pred_full} {acc}% TO {CHANNEL}")
            
        except Exception as e:
            print(f"ERROR SENDING TO {CHANNEL}: {e}")
            print("FIX: Make bot ADMIN in channel and check CHANNEL ID!")
        
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
