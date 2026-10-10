import asyncio
import random
import datetime
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@YOUR_CHANNEL_OR_ID"

symbols = [
"EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)",
"EUR/JPY (OTC)", "GBP/JPY (OTC)", "EUR/GBP (OTC)", "USD/CHF (OTC)",
"EUR/CHF (OTC)", "AUD/JPY (OTC)", "GBP/AUD (OTC)", "EUR/AUD (OTC)",
"USD/CAD (OTC)", "NZD/USD (OTC)", "GBP/CAD (OTC)", "EUR/CAD (OTC)",
"AUD/CAD (OTC)", "CAD/JPY (OTC)", "CHF/JPY (OTC)", "NZD/JPY (OTC)",
"AUD/CHF (OTC)", "AUD/NZD (OTC)", "CAD/CHF (OTC)", "EUR/NZD (OTC)",
"GBP/CHF (OTC)", "GBP/NZD (OTC)", "NZD/CAD (OTC)", "NZD/CHF (OTC)",
"EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/JPY", "GBP/JPY",
"EUR/GBP", "USD/CHF", "EUR/CHF", "AUD/JPY", "GBP/AUD", "EUR/AUD",
"USD/CAD", "NZD/USD", "GBP/CAD", "EUR/CAD", "AUD/CAD", "CAD/JPY",
"BTC/USD (OTC)", "ETH/USD (OTC)", "LTC/USD (OTC)", "BCH/USD (OTC)",
"XRP/USD (OTC)", "BNB/USD (OTC)", "ADA/USD (OTC)", "DOT/USD (OTC)",
"DOGE/USD (OTC)", "SOL/USD (OTC)", "BTC/USD", "ETH/USD",
"GOLD (OTC)", "SILVER (OTC)", "UKOIL (OTC)", "USOIL (OTC)"
]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            symbol = random.choice(symbols)
            is_up = random.choice([True, False])
            signal = "BUY 🟢 UP" if is_up else "SELL 🔴 DOWN"
            rsi = random.randint(25, 42) if is_up else random.randint(61, 84)
            acc = random.randint(90, 92)
            expiry = 1
            now = datetime.datetime.utcnow()
            entry_time = now + datetime.timedelta(minutes=1)
            received_str = now.strftime("%H:%M:%S")
            entry_str = entry_time.strftime("%H:%M:00")
            msg = f"""🔥 POCKET OPTION PREDICTION 🔥

📩 RECEIVED: {received_str} UTC
💰 PAIR: {symbol}
📊 PREDICTION: {signal}
📈 RSI: {rsi}
🎯 ACC
