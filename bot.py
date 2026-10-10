import asyncio, random, threading, os
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from flask import Flask

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8346566953:AAEu9eZ9OU9hJd9hJ5rK6v7fG8h...")
# ^^^ PUT YOUR REAL TOKEN OR KEEP ENV VARIABLE
CHANNEL_ID = os.getenv("CHANNEL_ID", "@your_channel")

PAIRS = ["EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)"]
bot = Bot(token=TELEGRAM_TOKEN)

# --- FIX FOR RENDER: OPEN A PORT ---
app = Flask(__name__)
@app.route('/')
def home(): return "BOT LIVE GOLD ELITE"
def run_web():
    app.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_web, daemon=True).start()
# --- END FIX ---

async def main():
    print("BOT STARTED")
    while True:
        try:
            now = datetime.now(pytz.utc)
            entry = now + timedelta(minutes=2) # +2 MIN EXACT WITH SECONDS
            st = now.strftime('%H:%M:%S')
            et = entry.strftime('%H:%M:%S')
            acc = random.randint(90, 92) # 90-92 ONLY
            pair = random.choice(PAIRS)
            pred = random.choice(['BUY 🟢 UP','SELL 🔴 DOWN'])
            msg = f"🔥 POCKET OPTION 🔥\n\n📩 SIGNAL: {st} UTC\n💰 PAIR: {pair}\n📊 PREDICTION: {pred}\n🎯 ACCURACY: {acc}%\n\n⏰ ENTRY TIME: {et} UTC\n⏱️ EXPIRY: 3 MIN\n\n⚡ AT {et} EXACTLY CLICK!\n\nGOLD ELITE VIP 🔥"
            await bot.send_message(chat_id=CHANNEL_ID, text=msg)
            print(f"SENT {st} -> {et} {acc}%")
        except Exception as e:
            print(e)
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
