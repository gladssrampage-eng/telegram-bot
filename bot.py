import telebot

TOKEN = "8683958931:AAF8wHkghFm6OVjynMzuKWN0ylZd0JTDQTA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(mensagem):
    bot.reply_to(mensagem, "🔥 Bot funcionando!")

bot.infinity_polling()
