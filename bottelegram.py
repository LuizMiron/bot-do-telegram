import telebot


CHAVE_API = "5674412007:AAGBw4atEbr4Kz7yuyyhTu8-3mh2ckoxtuE"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["help"])
def help(mensagem):
    texto = """comandos disponiveis
    /opcao1 : faz isso.
    /opcao2 : manda todas as informações da pessoa que mandou o comando.
    /opcao3 : manda uma mensagem."""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.reply_to(mensagem, "escolheu a opção1")
    
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, "escolheu a opção2 \n mandando informações do usuário:\n" + mensagem.from_user.first_name)
    
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "escolheu a opção3")
    

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = 'comando desconhecido, clique em: /help para ver as opções.'
    bot.reply_to(mensagem, texto)

bot.polling()
