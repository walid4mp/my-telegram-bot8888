import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# এখানে তোমার OpenAI API Key বসাও
OPENAI_API_KEY = "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"
# এখানে তোমার Telegram Bot Token বসাও
BOT_TOKEN = "7211528951:AAE6HSeyZz586kcyX-mM3kWq0tmKWrj0568"

openai.api_key = OPENAI_API_KEY

# /start কমান্ডে রিপ্লাই
def start(update, context):
    print(f"📩 /start কমান্ড পেয়েছি {update.effective_user.first_name} থেকে")
    update.message.reply_text("হ্যালো! আমি AI Telegram Bot 🤖। যা খুশি আমাকে জিজ্ঞেস করো।")

# AI উত্তর দেওয়ার ফাংশন
def ai_reply(update, context):
    user_text = update.message.text
    print(f"📩 মেসেজ পেয়েছি: {user_text}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        bot_text = response.choices[0].message["content"]
        print(f"🤖 উত্তর পাঠানো হলো: {bot_text}")
        update.message.reply_text(bot_text)
    except Exception as e:
        print(f"❌ এরর: {e}")
        update.message.reply_text("⚠️ সমস্যা হয়েছে: " + str(e))

# বট চালানো
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, ai_reply))

print("✅ Bot started and listening for messages...")
updater.start_polling()
updater.idle()

0

