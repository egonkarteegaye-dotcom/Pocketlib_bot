import os, time, random, threading
from flask import Flask
import requests
from datetime import datetime, timedelta
import pytz

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 GONKARTEE SON ROBOT LITE VIP IS LIVE 🔥"

def start_bot():
    print(f"DEBUG: TOKEN exists? {bool(TOKEN)}")
    print(f"DEBUG: CHANNEL exists? {CHANNEL}")
    if not TOKEN or not CHANNEL:
        print("❌ MISSING TOKEN OR CHANNEL_ID IN RENDER ENVIRONMENT!")
        return

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
⚡ PREPARATION TIME: 2 MINUTES"""

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = {"chat_id": CHANNEL, "text": msg}
            r = requests.post(url, data=data, timeout=10)
            print(f"✅ SENT {entry.strftime('%H:%M:%S')} -> {pair} {direction} {acc}% | Telegram response: {r.status_code}")
            if r.status_code!= 200:
                print(f"❌ TELEGRAM ERROR: {r.text}")

        except Exception as e:
            print(f"❌ ERROR: {e}")

        time.sleep(60)

threading.Thread(target=start_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
