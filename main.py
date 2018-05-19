#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import re
import constants
import random
import time
import reddit
import lastUsersMessage

# import requests
# def sendMessage(id, text):
#     requests.request('GET', 'https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text={2}'.format(token, id, text))

# sendMessage(224329635, "Fucker")
bot = telebot.TeleBot(constants.token)
print(bot.get_me())
# bot.send_message(103416615, "Your mom gay!")

lastUsersMessage = lastUsersMessage.Users


def searchForMomGay(msg):
    for i in range(11):
        if re.search(constants.YourMomGayArray[i], msg, re.IGNORECASE):
            return True


@bot.message_handler(commands=['meme'])
def handle_text(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    toSend = reddit.meme()
    print(toSend)
    while toSend == 'error':
        time.sleep(5)
        toSend = reddit.meme()
    if toSend != 'error':
        bot.send_photo(message.chat.id, toSend)


@bot.message_handler(commands=['kittens'])
def handle_text(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    toSend = reddit.cats()
    print(toSend)
    while toSend == 'error':
        time.sleep(5)
        toSend = reddit.cats();
    if toSend != 'error':
        bot.send_photo(message.chat.id, toSend)



@bot.message_handler(commands=['reddit'])
def handle_text(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    bot.set_update_listener('red')
    bot.send_message(message.chat.id, "Enter sub-reddit:")


@bot.message_handler(commands=['start'])
def handle_text(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row('/kittens', '/bsuirschedule')
    markup.row('/reddit', '/meme')
    markup.row('/flipcoin', '/help', '/stop')
    bot.send_message(message.chat.id, "Welcome!", reply_markup=markup)

# TODO
# @bot.message_handler(commands=['bsuirschedule'])
# def handle_text(message):
#     # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
#     markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     markup.row('/currentschedule')
#     btnReturn = telebot.types.KeyboardButton('<< BACK', '/start')
#     markup.row(btnReturn, '/setschedule')
#     bot.send_message(message.chat.id, "BSUIR Schedule", reply_markup=markup)


@bot.message_handler(commands=['changelog'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.changeLogg)
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)


@bot.message_handler(commands=['flipcoin'])
def handler(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    so = random.randint(0, 1)
    if so == 0:
        bot.send_message(message.chat.id, constants.heads)
    else:
        bot.send_message(message.chat.id, constants.tails)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.help)
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)


@bot.message_handler(commands=['stop'])
def handle_text(message):
    # lastUsersMessage.setLastMessage(lastUsersMessage, message.chat.id, message.text)
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Goodbye 😢. It was pleasure to help you.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if re.search("no u", message.text, re.IGNORECASE):
        bot.send_message(message.chat.id, "...")
    elif searchForMomGay(message.text):
        for i in range(11):
            if re.search(constants.YourMomGayArray[i], message.text, re.IGNORECASE):
                if i == 10:
                    bot.send_message(message.chat.id, "NO U!")
                else:
                    bot.send_message(message.chat.id, constants.YourMomGayArray[i + 1])
    elif re.search("u gay", message.text, re.IGNORECASE):
        bot.send_message(message.chat.id, "NO U!")
    else:
        # lastMessage = lastUsersMessage.lastMessage(self=lastUsersMessage, userId=message.chat.id)
        # print(lastMessage)
        if lastMessage == '/reddit':
            pass
            # post = reddit.reddit(message.text)
            # bot.send_photo(message.chat.id, post[0], post[1] + "\n" + post[2])
        else:
            bot.send_message(message.chat.id, "Sorry🙈, no such command!")


bot.polling(none_stop=True, interval=15)
