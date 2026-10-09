import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
DEST_CHANNEL = os.getenv("DEST_CHANNEL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ PocketLib2026_bot is running!")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")

async def forward_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.forward_message(chat_id=DEST_CHANNEL, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", get_id))
    app.add_handler(MessageHandler(filters.ALL, forward_handler))
    app.run_polling()
