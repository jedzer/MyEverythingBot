#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import re
import constants
import random
import time
import reddit
import usersGroup
import bsuirSchedule

bot = telebot.TeleBot(constants.token)
print(bot.get_me())



# lastUsersMessages = lastUsersMessage.UsersShit()


def searchForMomGay(msg):
    for i in range(11):
        if re.search(constants.YourMomGayArray[i], msg, re.IGNORECASE):
            return True


@bot.message_handler(commands=['meme'])
def handle_text(message):
    toSend = reddit.meme()
    while toSend == 'error':
        time.sleep(5)
        toSend = reddit.meme()
    if toSend != 'error':
        bot.send_photo(message.chat.id, toSend)


@bot.message_handler(commands=['kittens'])
def handle_text(message):
    toSend = reddit.cats()
    while toSend == 'error':
        time.sleep(5)
        toSend = reddit.cats();
    if toSend != 'error':
        bot.send_photo(message.chat.id, toSend)


@bot.message_handler(commands=['reddit'])
def handle_text(message):
    msg = bot.send_message(message.chat.id, "Enter sub-reddit:")
    bot.register_next_step_handler(msg, showReddit)
def showReddit(message):
    post = reddit.reddit(message.text)
    print(post)
    if post == "ERROR":
        bot.send_message(message.chat.id, "Can't reach that subReddit.")
    elif post[0] == "NOTANIMAGE":
        bot.send_message(message.chat.id, post[1] + "\n" + post[2])
    else:
        bot.send_photo(message.chat.id, post[0], post[1] + "\n" + post[2])

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row('/kittens', '/meme')
    markup.row('/bsuirschedule')
    markup.row('/reddit', '/flipcoin')
    markup.row('/help', '/stop')
    bot.send_message(message.chat.id, "MENU", reply_markup=markup)


@bot.message_handler(commands=['bsuirschedule'])
def schedule(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row('Current schedule', "This week")
    markup.row('BACK ', 'Set group')
    msg = bot.send_message(message.chat.id, "BSUIR Schedule", reply_markup=markup)
    bot.register_next_step_handler(msg, scheduleNext)

def scheduleNext(message):
    if message.text == "Current schedule":
        bot.send_message(message.chat.id, "Schedule: " + bsuirSchedule.getOneDaySchedule(message.chat.id))
        bot.register_next_step_handler(message, scheduleNext)
    elif message.text == "Set group":
        msg = bot.send_message(message.chat.id, "Enter group:")
        bot.register_next_step_handler(msg, setGroup)
    elif message.text == "This week":
        bot.send_message(message.chat.id, "This week:" + bsuirSchedule.getCurrentWeekSchedule(message.chat.id))
        bot.register_next_step_handler(message, scheduleNext)

    elif message.text == "BACK":
        msg = bot.send_message(message.chat.id, "Going back...")
        start(message)
    else:
        msg = bot.send_message(message.chat.id, "Wrong command")
        bot.register_next_step_handler(msg, scheduleNext)

def setGroup(message):
    bsuirSchedule.setUserGroupNumber(message.chat.id, message.text)
    msg = bot.send_message(message.chat.id, "--SET--")
    bot.register_next_step_handler(msg, scheduleNext)



@bot.message_handler(commands=['changelog'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.changeLogg)


@bot.message_handler(commands=['flipcoin'])
def handler(message):
    so = random.randint(0, 1)
    if so == 0:
        bot.send_message(message.chat.id, constants.heads)
    else:
        bot.send_message(message.chat.id, constants.tails)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, constants.help)


@bot.message_handler(commands=['stop'])
def handle_text(message):
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
        bot.send_message(message.chat.id, "Sorry🙈, no such command!")


bot.polling(none_stop=True, interval=0, timeout=5)
