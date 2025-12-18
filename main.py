from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7604811467:AAHh7_0qq-1OnsaUUOtuwFJzHhDaXbCfr_4"

# Raqam → video link
movie_links = {
    "1": "https://t.me/tatuda/5678",
    "2": "https://youtu.be/b1s-TZrfhRY?si=_wgCqirtZblWrUVc",  # Telegram video link
    "3": "https://www.youtube.com/watch?v=example3"
}

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎥 Kino botga xush kelibsiz!\n\n"
        "Quyidagi raqamlardan birini yuboring:\n"
        "1️⃣ Avatar (YouTube)\n"
        "2️⃣ Titanic (Telegram link)\n"
        "3️⃣ Interstellar (YouTube)\n\n"
        "Faqat raqam yuboring 👇"
    )
    await update.message.reply_text(text)

# Raqam yuborilganda video link yuborish
async def get_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if user_text in movie_links:
        await update.message.reply_text(
            f"🎬 Mana sizning kino:\n{movie_links[user_text]}"
        )
    else:
        await update.message.reply_text(
            "❌ Bunday raqam yo‘q. Iltimos, 1–3 oralig‘ida raqam yuboring."
        )

# Botni ishga tushirish
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_movie))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
