import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")
DEST = int(os.environ.get("DEST_CHANNEL_ID", "0"))

async def handle_all(update, context):
    if update.channel_post and update.channel_post.chat_id != DEST:
        try:
            await context.bot.copy_message(chat_id=DEST, from_chat_id=update.channel_post.chat_id, message_id=update.channel_post.message_id)
        except:
            pass

    if update.message and update.message.text and update.message.text.startswith("/start"):
        await update.message.reply_text("Bot is active!")

if __name__ == "__main__":
    if not TOKEN or not DEST:
        raise ValueError("Missing BOT_TOKEN or DEST_CHANNEL_ID env")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_all))
    app.run_polling(drop_pending_updates=True)
