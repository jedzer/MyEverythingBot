import telebot
import re
import constants

# import requests
# def sendMessage(id, text):
#     requests.request('GET', 'https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text={2}'.format(token, id, text))

# sendMessage(224329635, "Fucker")
bot = telebot.TeleBot(constants.token)
print(bot.get_me())
# bot.send_message(103416615, "Your mom gay!")

changeLogg = "1. Added your mum gay"
YourMomGayArray = ["Ur mum gay",
                    "Ur dad lesbian",
                    "Ur brother a mother",
                    "Ur sister a mister",
                    "Ur granny tranny",
                    "Ur grandap a tap",
                    "Ur family tree lgbt",
                    "Ur ancestors incestors",
                    "Ur species feces",
                    "Ur genus likes penis",
                    "Ur family reunion homosexual communion"]

def SearchForMomGay(msg):
    for i in range(11):
        if re.search(YourMomGayArray[i], msg, re.IGNORECASE):
            return True


@bot.message_handler(commands=['changelog'])
def handle_text(message):
    bot.send_message(message.chat.id, changeLogg)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if re.search("no u", message.text, re.IGNORECASE):
        bot.send_message(message.chat.id, "...")
    elif SearchForMomGay(message.text):
        for i in range(11):
            if re.search(YourMomGayArray[i], message.text, re.IGNORECASE):
                if i == 10:
                    bot.send_message(message.chat.id, "NO U!")
                else:
                    bot.send_message(message.chat.id, YourMomGayArray[i + 1])
    elif re.search("u gay", message.text, re.IGNORECASE):
        bot.send_message(message.chat.id, "NO U!")
    else:
        bot.send_message(message.chat.id, "Sorry, no such command!")


bot.polling(none_stop=True, interval=0)
