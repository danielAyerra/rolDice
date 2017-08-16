import telebot
import random
import common


rolzCaller = telebot.TeleBot('*********************')


@rolzCaller.message_handler(commands=['start'])
def send_welcome(message):
    rolzCaller.reply_to(message, "A Jugar!!!!")
    common.worksBool = True


@rolzCaller.message_handler(commands=['help'])
def send_help(message):
    if common.worksBool is True:
        rolzCaller.reply_to(message,
        "If you type me /roll xdy, "
        "x=number of dice e y=type of die, maybe I shall obey ;)")


@rolzCaller.message_handler(commands=['roll'])
def send_ask_dice(message):
    if common.worksBool is True:
        messageExtract = str(message.text)
        print(messageExtract)
        messageTreated = messageExtract.replace('/roll ', '')
        try:
            numberOfDice = int(messageTreated.split('d')[0])
            typeOfDie = int(messageTreated.split('d')[1])
        except ValueError:
            rolzCaller.reply_to(message,"Hey, Buddy, where are my dice?")
            numberOfDice = 0
            typeOfDie = 0
        totalAnswer = 0
        rolled = []
        if typeOfDie == 4 or typeOfDie == 6 or typeOfDie == 8 or typeOfDie == 10 or typeOfDie == 12 or typeOfDie == 20 or typeOfDie == 100:
            for i in range(0, numberOfDice):
                x = random.randint(1, typeOfDie)
                rolled.append(x)
                totalAnswer = totalAnswer + x
            rolzCaller.reply_to(message, "Time(s) {} Total Add: {}".format(rolled, totalAnswer))
        else:
            rolzCaller.reply_to(message, "Buddy, sthing is wrong... Repeat")


@rolzCaller.message_handler(commands=['stop'])
def send_goodbye(message):
    if common.worksBool is True:
        rolzCaller.reply_to(message, "Game Over :(")
        common.worksBool = False



@rolzCaller.message_handler(func=lambda message: True)
def echo_all(message):
    if common.worksBool is True:
        rolzCaller.reply_to(message, "Did ya say sthing?")

rolzCaller.polling()
    rolzCaller.reply_to(message, "Let's GO!!!!")


    

        
 
   
        


   




