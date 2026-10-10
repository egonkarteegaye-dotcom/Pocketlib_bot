import asyncio, random, threading, os
from datetime import datetime, timedelta
import pytz
from telegram import Bot
from flask import Flask

# --- ENV FROM RENDER - DON'T CHANGE ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")
if not TOKEN or not CHANNEL:
    print("ERROR: Set TELEGRAM_TOKEN and CHANNEL_ID in Render Environment!")
    # Fallback for testing
    TOKEN = "8434602399:AAH-6K4m3K5a5a5a_REPLACE"
    CHANNEL = "@REPLACE"

bot = Bot(token=TOKEN)

app = Flask(__name__)
@app.route('/')
def home(): 
    return "GONKARTEE SON ROBOT LITE VIP 🔥 💵 LIVE - 90-95% ACCURACY"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_web, daemon=True).start()

PAIRS = [
   
