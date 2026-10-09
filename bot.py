import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
DEST_CHANNEL = os.getenv("DEST_CHANNEL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ PocketLib Bot is Live!\n\nUse /id to get chat IDs")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Chat ID: `{chat_id}`", parse_mode="Markdown")

async def forward_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if SOURCE_CHANNEL and str(update.effective_chat.id) == str(SOURCE_CHANNEL):
            if DEST_CHANNEL:
                await context.bot.forward_message(
                    chat_id=DEST_CHANNEL,
                    from_chat_id=update.effective_chat.id,
                    message_id=update.message.message_id
                )
    except Exception as e:
        logging.error(f"Forward error: {e}")

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not set!")
        exit(1)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(MessageHandler(filters.ALL, forward_handler))
    print("Bot starting...")
    app.run_polling()
