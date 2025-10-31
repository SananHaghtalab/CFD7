from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from modules import config  # چون config.py داخل پوشه modules هست

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام سانان! بات CFD7 فعال شد ✅")

app = ApplicationBuilder().token(config.BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
