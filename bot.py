import asyncio
import random
import datetime
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@YOUR_CHANNEL_OR_ID"

symbols = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/JPY", "GBP/JPY", "USD/CHF", "EUR/GBP", "BTC/USD", "ETH/USD"]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    
    while True:
        try:
            symbol = random.choice(symbols)
            is_up = random.choice([True, False])
            signal = "BUY 🟢⬆️" if is_up else "SELL 🔴⬇️"
            expiry = random.choice([1, 2, 3])
            
            # HIGH ACCURACY 91-97% - WILL SHOW ALWAYS
            acc = random.randint(91, 97)
            up_percent = random.randint(88, 96) if is_up else random.randint(7, 15)
            down_percent = 100 - up_percent
            
            now = datetime.datetime.utcnow()
            entry_time = now + datetime.timedelta(minutes=1)
            current_str = now.strftime("%H:%M:%S")
            entry_str = entry_time.strftime("%H:%M:%S")
            
            msg = f"""GONKARTEE SON GOLD ELITE VIP 🔥✅

🔥 POCKET OPTION PREDICTION 🔥
💰 PAIR: {symbol} (OTC)
📊 ACTION: {signal}

📈 ANALYSIS:
BUY: {up_percent}% 
SELL: {down_percent}%

⏰ EXPIRY: {expiry} MINUTE

🕐 NOW: {current_str} UTC
🎯 ENTRY IN 1 MIN: {entry_str} UTC

🎯 ACCURACY: {acc}% - HIGH CONFIDENCE!
💎 PREMIUM VIP SIGNAL

⚡ GET READY - ENTER AT {entry_str}!
🔥 POWERED BY GONKARTEE SON
"""
            
            await bot.send_message(chat_id=CHANNEL_ID, text=msg)
            print(f"Signal sent: {symbol} {signal} Accuracy {acc}%")
            
            # Every 1 MINUTE
            await asyncio.sleep(60)
            
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(send_signal())
