#pip install pytelegrambotapi

import telebot

'''
Entrar no telegram , pesquisar por bot father, depois va em new bot de um nome,depois de mais um
nick com final bot.
Vai devolver um token HTTP basta copia-lo
'''

CHAVE_API = "1912159978:AAGXZGu1cMTcsWDPz2KSjfPDRdo96H7jPaA"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['calabresa'])
def response(msg):
    bot.send_message(msg.chat.id,'Saindo a pizza para sua casa')


@bot.message_handler(commands=['catupiry'])
def response(msg):
    bot.send_message(msg.chat.id,'Saindo a pizza para sua casa')

@bot.message_handler(commands=['4queijos'])
def response(msg):
    bot.send_message(msg.chat.id,'Saindo a pizza para sua casa')

@bot.message_handler(commands=['modadacasa'])
def response(msg):
    bot.send_message(msg.chat.id,'Saindo a pizza para sua casa')

@bot.message_handler(commands=['chocolate'])
def response(msg):
    bot.send_message(msg.chat.id,'Saindo a pizza para sua casa')
    
@bot.message_handler(commands=['opcao1'])
def response(msg):
    texto='''
    Qual sabor de pizza deseja?
    /calabresa Calabresa
    /catupiry Catupiry
    /4queijos 4Queijos
    /modadacasa ModaDaCasa
    /chocolate Chocolate
    '''
    bot.send_message(msg.chat.id,texto)

@bot.message_handler(commands=['opcao2'])
def response(msg):
    bot.send_message(msg.chat.id,'Para fazer uma reclamação, mande um e-mail para reclamações@gmail.com')

@bot.message_handler(commands=['opcao3'])
def response(msg):
    #Essa menssagem mostra tudo que pode ser usado, em forma de dicionario
    print(msg)
    bot.send_message(msg.chat.id,'Valeu! O Victor está mandando um abraço de volta ',msg.chat.first_name)

#Essas duas funções precisam sempre ser as ultimas
def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def response(msg):
    texto='''
            Escolha uma opção abaixo para continuar:
            /opcao1 Fazer um pedido
            /opcao2 Reclamar de um pedido
            /opcao3 mandar uma abraço para o Victor
        Responder qualquer coutra coisa não vai funcionar, clieque em uma das opções
    '''
    bot.reply_to(msg,texto)
    


#Loop infinito, para ficar escutando conversas
bot.polling()


