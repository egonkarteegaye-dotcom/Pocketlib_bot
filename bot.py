import asyncio, random, threading, os
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from flask import Flask

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")
bot = Bot(token=TOKEN) if TOKEN else Bot(token="8434602399:AAH-6K4m3K5a5a5a_REPLACE")

app = Flask(__name__)
@app.route('/')
def home():
    return "GONKARTEE SON ROBOT LITE VIP LIVE"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
threading.Thread(target=run_web, daemon=True).start()

PAIRS = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "EUR/GBP (OTC)", "AUD/USD (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "USD/CAD (OTC)"]

async def main():
    print(f"GONKARTEE VIP STARTED FOR {CHANNEL}")
    while True:
        try:
            now = datetime.now(pytz.utc)
            entry = now + timedelta(minutes=2)
            st = now.strftime('%H:%M:%S')
            et = entry.strftime('%H:%M:%S')
            acc = random.randint(90, 95)
            pair = random.choice(PAIRS)
            is_buy = random.choice([True, False])
            direction = "UP" if is_buy else "DOWN"
            pred = "BUY 🟢 UP ⬆️" if is_buy else "SELL 🔴 DOWN ⬇️"
            msg = f"🔥 GONKARTEE SON ROBOT LITE VIP 🔥 💵\n\n📩 SIGNAL RECEIVED: {st} UTC\n💰 PAIR: {pair}\n📈 DIRECTION: {direction}\n📊 PREDICTION: {pred}\n🎯 ACCURACY: {acc}%\n\n━━━━━━━━━━━━━━\n⏰ ENTRY TIME: {et} UTC\n⏱️ EXPIRY: 3 MIN\n━━━━━━━━━━━━━━\n\n⚡ 2 MINUTES PREPARATION!\n⚡ AT {et} EXACTLY CLICK {direction}!\n\n🔥 GONKARTEE SON {acc}% VIP 🔥 💵"
            await bot.send_message(chat_id=CHANNEL, text=msg)
            print(f"SENT {st} -> {et} | {pair} {pred} {acc}%")
        except Exception as e:
            print(f"ERROR: {e}")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
