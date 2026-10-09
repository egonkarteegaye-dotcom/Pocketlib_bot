import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
BOT_TOKEN=os.getenv("BOT_TOKEN")
DEST=os.getenv("DEST_CHANNEL")
async def start(u,c): await u.message.reply_text("Bot Live! Send /id in channel")
async def get_id(u,c): await u.message.reply_text(f"ID: {u.effective_chat.id}")
async def fwd(u,c):
 if u.channel_post:
  try: await c.bot.copy_message(chat_id=DEST, from_chat_id=u.channel_post.chat_id, message_id=u.channel_post.message_id)
  except: pass
app=ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("id",get_id))
app.add_handler(MessageHandler(filters.ALL,fwd))
app.run_polling()
