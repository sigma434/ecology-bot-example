import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.handler_backends import ContinueHandling
from telebot import types


bot = telebot.TeleBot("YOUR TOKEN")


bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("text", "sending you a text about ecology"),
        telebot.types.BotCommand("start","greets you"),
        telebot.types.BotCommand("help","sends you a command list"),
        telebot.types.BotCommand("subotnik"," sends you site with dates")
        ])


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "В боте есть следующие команды : /start и /text и /subotnik")

@bot.message_handler(commands=["subotnik"])
def subotnik(message):
    bot.send_message(message.chat.id, "Даты с суботниками в москве: https://www.mos.ru/mayor/themes/12531050/")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который расскажет тебе про проблемы о нынешней экологии.")


@bot.message_handler(commands=["text"])
def text(message):
    text=open("text.txt" ,"r",encoding="utf-8")
    f=text.read()
    bot.send_message(message.chat.id , f )
    text.close()
 

bot.infinity_polling()
