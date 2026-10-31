import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from googletrans import Translator

# লগিং সেটআপ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

translator = Translator()

# মেসেজ হ্যান্ডলার ফাংশন
async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    try:
        # ইংরেজি থেকে বাংলায় অনুবাদ করা
        translation = translator.translate(user_text, dest='bn')
        await update.message.reply_text(translation.text)
    except Exception as e:
        await update.message.reply_text("দুঃখিত, অনুবাদ করতে সমস্যা হয়েছে।")

if __name__ == '__main__':
    # আপনার BotFather থেকে পাওয়া টোকেন এখানে বসাবেন
    TOKEN = "9262556298:AAHHg2Ww5wnHtW1qk6P1Uta6sYaC9_0Ki5k"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    # যেকোনো টেক্সট মেসেজ ফিল্টার করে অনুবাদ ফাংশনে পাঠানো
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), translate_text))
    
    print("বট চালু হয়েছে...")
    app.run_polling()
    