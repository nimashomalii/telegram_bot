from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ✅ توکن رباتت
TOKEN = "6919651213:AAFkVvVXFVVWZLn19U8zDC4oKQ2x-Ceuhhk"

# ✅ تابع پاسخ‌دهی به هر پیام
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi")

# ✅ اجرای ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    app.add_handler(message_handler)

    print("Bot is running...")
    app.run_polling()
