import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive - GOLD ELITE VIP")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

Thread(target=run_dummy_server, daemon=True).start()

from telegram.ext import ApplicationBuilder, MessageHandler, filters, ChannelPostHandler
import asyncio

TOKEN = os.environ.get("BOT_TOKEN")
DEST = int(os.environ.get("DEST_CHANNEL_ID", "-1004292216492"))

async def handle_all(update, context):
    try:
        if update.channel_post:
            await context.bot.copy_message(
                chat_id=DEST,
                from_chat_id=update.channel_post.chat_id,
                message_id=update.channel_post.message_id
            )
    except:
        pass

    if update.message and update.message.text:
        try:
            if update.message.text.lower() == "/start":
                await update.message.reply_text("Bot is Live ✅ GOLD ELITE VIP is working!")
        except:
            pass

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChannelPostHandler(handle_all))
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    print("Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
