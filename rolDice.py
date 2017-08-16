import telebot
import random

rolzCaller = telebot.TeleBot('*********:######################')


@rolzCaller.message_handler(commands=['start'])
def send_welcome(message):
    rolzCaller.reply_to(message, "A Jugar!!!!")

@rolzCaller.message_handler(commands=['help'])
def send_help(message):
    rolzCaller.reply_to(message,
    "Si me escribes roll y xdy, "
    "x=numero de dados e y=tipo de dado, te hare caso ;)")

@rolzCaller.message_handler(commands=['roll'])
def send_ask_dice(message):
    messageExtract = str(message.text)
    print(messageExtract)
    messageTreated = messageExtract.replace('/roll ', '')
    try:
        numberOfDice = int(messageTreated.split('d')[0])
        typeOfDie = int(messageTreated.split('d')[1])
    except ValueError:
        rolzCaller.reply_to(message,"Incluye dados, colega")
        numberOfDice = 0
        typeOfDie = 0

    print("Dados {} Tipo de dado {}.".format(numberOfDice, typeOfDie))
    totalAnswer = 0
    rolled = []
    if typeOfDie == 4 or typeOfDie == 6 or typeOfDie == 8 or typeOfDie == 10 or typeOfDie == 12 or typeOfDie == 20 or typeOfDie == 100:
        for i in range(0, numberOfDice):
            x = random.randint(1, typeOfDie)
            rolled.append(x)
            totalAnswer=totalAnswer+x
        rolzCaller.send_message(-*************, "Tirada(s) {} Suma total: {}".format(rolled, totalAnswer))
    else:
        rolzCaller.reply_to(message, "Colega, no te pillo... Repite")

@rolzCaller.message_handler(commands=['stop'])
def send_welcome(message):
    rolzCaller.reply_to(message, "Game Over :(")

@rolzCaller.message_handler(func=lambda message: True)
def echo_all(message):
    rolzCaller.reply_to(message, "Habla, chucho, que no te escucho!!")

rolzCaller.polling()

