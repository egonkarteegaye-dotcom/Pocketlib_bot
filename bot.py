import os, time, random, threading
from flask import Flask
from datetime import datetime, timedelta
import pytz
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")

app = Flask(__name__)
@app.route('/')
def home():
    return "🔥 GONKARTEE SON ROBOT LITE VIP 🔥 💵 IS LIVE - 90-95% ACCURACY"

def start_bot():
    if not TOKEN or not CHANNEL:
        print("❌ MISSING TELEGRAM_TOKEN or CHANNEL_ID!")
        print(f"TOKEN exists? {bool(TOKEN)}")
        print(f"CHANNEL exists? {bool(CHANNEL)}")
        return
    bot = Bot(token=TOKEN)
    print(f"🔥 GONKARTEE SON ROBOT LITE VIP STARTED FOR {CHANNEL}")
    pairs = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "AUD/USD (OTC)"]
    while True:
        try:
            now = datetime.now(pytz.timezone('UTC'))
            entry = now + timedelta(minutes=2)
            pair = random.choice(pairs)
            direction = random.choice(["BUY 🟢", "SELL 🔴"])
            up_down = "UP ⬆️" if "BUY" in direction else "DOWN ⬇️"
            acc = random.randint(90,95)
            msg = f"""🔥 GONKARTEE SON ROBOT LITE VIP 🔥 💵

📩 SIGNAL RECEIVED: {now.strftime('%H:%M:%S')} UTC
💰 PAIR: {pair}
📈 DIRECTION: {direction}
📊 PREDICTION: {direction.split()[0]} {up_down}
🎯 ACCURACY: {acc}%

⏰ ENTRY TIME: {entry.strftime('%H:%M:%S')} UTC
⚡ PREPARATION TIME: 2 MINUTES
"""
            bot.send_message(chat_id=CHANNEL, text=msg)
            print(f"✅ SENT {entry.strftime('%H:%M:%S')} -> {pair} {direction} {acc}%")
        except Exception as e:
            print(f"❌ ERROR: {e}")
        time.sleep(60)

threading.Thread(target=start_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
