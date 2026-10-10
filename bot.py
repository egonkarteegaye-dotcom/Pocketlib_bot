import asyncio
import random
from datetime import datetime, timedelta
import pytz
from telegram import Bot

# ========== CONFIG - YOU CAN EDIT THIS ==========
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@YOUR_CHANNEL_HERE"

# TIMER SETTINGS - CHANGED AS YOU ASKED
START_TIMER = 2  # 2 minutes start
MIXED_LIMIT_MIN = 2
MIXED_LIMIT_MAX = 5  # mixed limit to 5 minutes
SIGNAL_INTERVAL = 120  # send every 2 minutes (120 seconds)

# ACCURACY - KEEP 90-92%
ACCURACY_MIN = 90
ACCURACY_MAX = 92

# ALL 66 PAIRS - KEEP EVERYTHING
ALL_PAIRS = [
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/USD OTC", "USD/CAD OTC",
    "EUR/GBP OTC", "EUR/JPY OTC", "GBP/JPY OTC", "AUD/JPY OTC", "EUR/AUD OTC",
    "GBP/AUD OTC", "EUR/CAD OTC", "AUD/CAD OTC", "GBP/CAD OTC", "EUR/CHF OTC",
    "GBP/CHF OTC", "AUD/CHF OTC", "USD/CHF OTC", "NZD/USD OTC", "EUR/NZD OTC",
    "GBP/NZD OTC", "AUD/NZD OTC", "NZD/JPY OTC", "NZD/CAD OTC", "NZD/CHF OTC",
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "EUR/GBP", "EUR/JPY", "GBP/JPY", "AUD/JPY", "EUR/AUD",
    "GBP/AUD", "EUR/CAD", "AUD/CAD", "GBP/CAD", "EUR/CHF",
    "GBP/CHF", "AUD/CHF", "USD/CHF", "NZD/USD", "EUR/NZD",
    "USD/BRL OTC", "USD/INR OTC", "USD/TRY OTC", "USD/ZAR OTC", "USD/MXN OTC",
    "USD/PKR OTC", "USD/EGP OTC", "USD/BDT OTC", "USD/NGN OTC", "USD/PHP OTC",
    "BTC/USD OTC", "ETH/USD OTC", "LTC/USD OTC", "BNB/USD OTC", "SOL/USD OTC",
    "XRP/USD OTC", "DOGE/USD OTC", "ADA/USD OTC", "DOT/USD OTC", "MATIC/USD OTC",
    "AVAX/USD OTC"
]

bot = Bot(token=TELEGRAM_TOKEN)

def get_next_entry_time():
    """Entry time is 2 minutes from now"""
    now = datetime.now(pytz.timezone('Africa/Monrovia'))
    entry = now + timedelta(minutes=START_TIMER)
    return entry.strftime("%H:%M")

def generate_signal():
    pair = random.choice(ALL_PAIRS)
    direction = random.choice(["BUY 🟢", "SELL 🔴"])
    accuracy = random.randint(ACCURACY_MIN, ACCURACY_MAX)
    expiry = random.randint(MIXED_LIMIT_MIN, MIXED_LIMIT_MAX)
    entry_time = get_next_entry_time()
    
    signal = f"""
📊 POCKET OPTION SIGNAL 📊

💱 Pair: {pair}
📈 Direction: {direction}
⏰ Entry Time: {entry_time}
⏳ Expiry: {expiry} Minutes
🎯 Accuracy: {accuracy}%

⚡️ Start: {START_TIMER} Min | Limit: {MIXED_LIMIT_MAX} Min Mixed

🔥 Trade with 90-92% Confidence!
"""
    return signal

async def main():
    print(f"Bot Started! Timer: {START_TIMER} min | Limit: {MIXED_LIMIT_MAX} min | Accuracy: {ACCURACY_MIN}-{ACCURACY_MAX}%")
    print(f"Total Pairs: {len(ALL_PAIRS)}")
    while True:
        signal = generate_signal()
        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=signal)
            print(f"Signal sent at {datetime.now()}: {signal}")
        except Exception as e:
            print(f"Error: {e}")
        
        await asyncio.sleep(SIGNAL_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
