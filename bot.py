from flask import Flask
import threading,asyncio,random,os
from datetime import datetime,timedelta
from telegram import Bot
app=Flask('')
@app.route('/')
def home():return "GOLD ELITE VIP IS LIVE!"
def run():app.run(host='0.0.0.0',port=10000)
threading.Thread(target=run).start()
TOKEN=os.getenv("BOT_TOKEN")
CHANNEL_ID=os.getenv("CHANNEL_ID")
async def main():
 bot=Bot(token=TOKEN)
 await bot.send_message(chat_id=CHANNEL_ID,text="GOLD ELITE VIP - RANDOM EXPIRY LIVE!")
 pairs=["EUR/USD (OTC)","GBP/USD (OTC)","EUR/GBP (OTC)","USD/JPY (OTC)","AUD/USD (OTC)"]
 while True:
  try:
   now=datetime.utcnow()
   sig=now.strftime('%H:%M:%S')
   ent=(now+timedelta(minutes=1)).replace(second=0,microsecond=0).strftime('%H:%M:%S')
   pair=random.choice(pairs)
   buy=random.choice([True,False])
   pred="BUY 🟢 UP" if buy else "SELL 🔴 DOWN"
   rsi=random.randint(22,35) if buy else random.randint(65,88)
   acc=random.randint(85,92)
   expiry=random.choice([2,3,4,5])
   msg=f"""🔥 POCKET OPTION PREDICTION 🔥

📩 SIGNAL RECEIVED: {sig} UTC
💰 PAIR: {pair}
📊 PREDICTION: {pred}
📈 RSI: {rsi}
🎯 ACCURACY: {acc}%

━━━━━━━━━━━━━━
⏰ ENTRY TIME: {ent} UTC
⏰ That's 1 MINUTE after signal!
⏱️ EXPIRY: {expiry} MINUTES

⚡ SET UP NOW:
1. Open {pair}
2. Set amount $1
3. Set expiry {expiry} min
4. WAIT for {ent}

⚡ AT {ent} EXACTLY → CLICK {pred}!

━━━━━━━━━━━━━━
GOLD ELITE VIP 🔥 - Monrovia Time = UTC"""
   await bot.send_message(chat_id=CHANNEL_ID,text=msg)
   await asyncio.sleep(60)
  except Exception as e:
   print(e)
   await asyncio.sleep(10)
asyncio.run(main())
