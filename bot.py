import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import asyncio

# --- FREE RENDER FIX: Open port immediately ---
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive - GOLD ELITE VIP")
    def log_message(self, *args):
        return

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Dummy server listening on {port}")
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
# --- END FIX ---

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
DEST_CHANNEL_ID = os.environ.get("DEST_CHANNEL_ID")

async def handle_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        try:
            await update.effective_message.copy(chat_id=DEST_CHANNEL_ID)
        except Exception as e:
            print(f"Copy error: {e}")

async def main():
    if not BOT_TOKEN or not DEST_CHANNEL_ID:
        print("Missing BOT_TOKEN or DEST_CHANNEL_ID in Environment!")
        # Keep server alive even if token missing
        while True:
            await asyncio.sleep(3600)
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    print("Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
