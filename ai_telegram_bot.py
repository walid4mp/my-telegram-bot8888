import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# তোমার API KEY
OPENAI_API_KEY = "তোমার_OPENAI_API_KEY"
BOT_TOKEN = "তোমার_TELEGRAM_BOT_TOKEN"

openai.api_key = OPENAI_API_KEY

def start(update, context):
    update.message.reply_text("হ্যালো! আমি AI Bot 🤖। যা খুশি আমাকে জিজ্ঞেস করো।")

def ai_reply(update, context):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    bot_text = response.choices[0].message["content"]
    update.message.reply_text(bot_text)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

OPENAI_API_KEY = "নতুন_OPENAI_API_KEY"
BOT_TOKEN = "নতুন_TELEGRAM_BOT_TOKEN"
Xdp.add_handler(CommandHandler("start", start))xit

dp.add_handler(MessageHandler(Filters.text, ai_reply))

updater.start_polling()
updater.idle()

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

7211528951:AAHMdI8ZfvDwjHk_rA1A5k0TY2kHz7FEzP4

