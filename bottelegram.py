import telebot


CHAVE_API = "5674412007:AAGBw4atEbr4Kz7yuyyhTu8-3mh2ckoxtuE"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá aqui é bot do luiz")

bot.polling()
