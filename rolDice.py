import telebot
import random

rolzCaller = telebot.TeleBot('*************:###################')


@rolzCaller.message_handler(commands=['start'])
def send_welcome(message):
    rolzCaller.reply_to(message, "Let's GO!!!!")

@rolzCaller.message_handler(commands=['help'])
def send_help(message):
    rolzCaller.reply_to(message,
    "If you type me /roll xdy, "
    "x=number of dice e y=type of die, maybe I shall obey ;)")

@rolzCaller.message_handler(commands=['roll'])
def send_ask_dice(message):
    messageExtract = str(message.text)
    print(messageExtract)
    messageTreated = messageExtract.replace('/roll ', '')
    numberOfDice = int(messageTreated.split('d')[0])
    typeOfDie = int(messageTreated.split('d')[1])
    print("Dados {} Tipo de dado {}.".format(numberOfDice, typeOfDie))
    totalAnswer = 0
    rolled = []
    if typeOfDie == 4 or typeOfDie == 6 or typeOfDie == 8 or typeOfDie == 10 or typeOfDie == 12 or typeOfDie == 20 or typeOfDie == 100:
        for i in range(0, numberOfDice):
            x = random.randint(1, typeOfDie)
            rolled.append(x)
            totalAnswer=totalAnswer+x
        rolzCaller.send_message(-1001121407949, "Tirada(s) {} Suma total: {}".format(rolled, totalAnswer))
    else:
        rolzCaller.reply_to(message, "Buddy, sthing is wrong... Repeat")

@rolzCaller.message_handler(commands=['stop'])
def send_welcome(message):
    rolzCaller.reply_to(message, "Game Over :(")

@rolzCaller.message_handler(func=lambda message: True)
def echo_all(message):
    rolzCaller.reply_to(message, "Did ya say sthing?")

rolzCaller.polling()
