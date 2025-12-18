import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")  # ❗ token endi serverdan olinadi

movie_links = {
    "1": "https://t.me/tatuda/5678",
    "2": "https://youtu.be/b1s-TZrfhRY?si=_wgCqirtZblWrUVc",
    "3": "https://www.youtube.com/watch?v=example3"
}

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

async def get_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()

    if user_text in movie_links:
        await update.message.reply_text(
            f"🎬 Mana sizning kino:\n{movie_links[user_text]}"
        )
    else:
        await update.message.reply_text(
            "❌ Bunday raqam yo‘q.
