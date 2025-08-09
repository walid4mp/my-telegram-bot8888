from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import base64

TOKEN = "7211528951:AAEulvdqpisjV9Lo6P8NfzGRhJ2HK3aHjN4"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি OSINT & Tools বট। /tools দিয়ে সব কমান্ড দেখুন।")

# /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ Bot Information:\nDeveloper: Tanvir\nType: OSINT & Tools Bot")

# /ipinfo <ip>
async def ipinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /ipinfo <IP>")
        return
    ip = context.args[0]
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    await update.message.reply_text(str(res))

# /tools
async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🛠 Available Commands:
/start
/info
/ipinfo <ip>
/osi
/iptrack <ip>
/emailverify <email>
/userlookup <username>
/encode <text>
/reversehash <hash>
/linkshort <url>
/decodeb64 <text>
/b64 <text>
/subdomain <domain>
/dns <domain>
""")

# /osi
async def osi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 OSINT (Open Source Intelligence) টুলস অ্যাক্টিভ আছে। /tools কমান্ড ব্যবহার করুন।")

# /iptrack
async def iptrack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /iptrack <IP>")
        return
    ip = context.args[0]
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    await update.message.reply_text(str(res))

# /emailverify
async def emailverify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /emailverify <email>")
        return
    email = context.args[0]
    await update.message.reply_text(f"📧 {email} ইমেইল চেক সিস্টেমে যুক্ত করা হয়নি (ডেমো মোড)।")

# /userlookup
async def userlookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /userlookup <username>")
        return
    username = context.args[0]
    await update.message.reply_text(f"🔍 {username} ইউজারনেম চেক সিস্টেমে যুক্ত করা হয়নি (ডেমো মোড)।")

# /encode
async def encode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /encode <text>")
        return
    text = " ".join(context.args)
    encoded = base64.b64encode(text.encode()).decode()
    await update.message.reply_text(f"✅ Encoded: {encoded}")

# /reversehash
async def reversehash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ রিভার্স হ্যাশ API যুক্ত করা হয়নি (ডেমো মোড)।")

# /linkshort
async def linkshort(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /linkshort <url>")
        return
    url = context.args[0]
    res = requests.get(f"http://tinyurl.com/api-create.php?url={url}").text
    await update.message.reply_text(f"🔗 Short URL: {res}")

# /decodeb64
async def decodeb64(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /decodeb64 <text>")
        return
    text = context.args[0]
    decoded = base64.b64decode(text).decode()
    await update.message.reply_text(f"✅ Decoded: {decoded}")

# /b64
async def b64(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("⚠️ ব্যবহার: /b64 <text>")
        return
    text = context.args[0]
    encoded = base64.b64encode(text.encode()).decode()
    await update.message.reply_text(f"✅ Base64: {encoded}")

# /subdomain
async def subdomain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ সাবডোমেইন স্ক্যানার যুক্ত করা হয়নি (ডেমো মোড)।")

# /dns
async def dns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ DNS লুকআপ সিস্টেম যুক্ত করা হয়নি (ডেমো মোড)।")

# Bot চালানো
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("ipinfo", ipinfo))
app.add_handler(CommandHandler("tools", tools))
app.add_handler(CommandHandler("osi", osi))
app.add_handler(CommandHandler("iptrack", iptrack))
app.add_handler(CommandHandler("emailverify", emailverify))
app.add_handler(CommandHandler("userlookup", userlookup))
app.add_handler(CommandHandler("encode", encode))
app.add_handler(CommandHandler("reversehash", reversehash))
app.add_handler(CommandHandler("linkshort", linkshort))
app.add_handler(CommandHandler("decodeb64", decodeb64))
app.add_handler(CommandHandler("b64", b64))
app.add_handler(CommandHandler("subdomain", subdomain))
app.add_handler(CommandHandler("dns", dns))

app.run_polling()
