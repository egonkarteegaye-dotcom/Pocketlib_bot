import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN=os.getenv("BOT_TOKEN")
DEST=os.getenv("DEST_CHANNEL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is Live!")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")

async def forward_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        try:
            await context.bot.copy_message(chat_id=DEST, from_chat_id=update.channel_post.chat_id, message_id=update.channel_post.message_id)
        except:
            pass

app=ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("id", get_id))
app.add_handler(MessageHandler(filters.ALL, forward_channel))
app.run_polling()
