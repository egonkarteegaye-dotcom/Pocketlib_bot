import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive - GOLD ELITE VIP")
    def log_message(self,*a): return

def run_server():
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT",10000))), Handler).serve_forever()
threading.Thread(target=run_server, daemon=True).start()

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN=os.environ.get("BOT_TOKEN")
DEST_CHANNEL_ID=os.environ.get("DEST_CHANNEL_ID")

async def handle_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        try:
            await update.effective_message.copy(chat_id=DEST_CHANNEL_ID)
        except Exception as e:
            print(e)

def main():
    app=ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    app.run_polling()

if __name__=="__main__":
    main()
