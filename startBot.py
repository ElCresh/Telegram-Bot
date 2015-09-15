#!/usr/bin/env python
#
# Telegram Bot r0.1
#
# Copyright (C) 2015
#
# Authors:
# Andrea Crescentini <cresh.it@gmail.com>
# Andrea Bartolucci <andbartol>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import MySQLdb
import telegram
import sys

## DATABASE CONNECTION INFO ##
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "root"
MYSQL_DB = "telegram_bot"
MYSQL_REPLY_TABLE = "reply"
##############################

###### BOT INFO VARIABLE ######
TELEGRAM_BOT_NAME = ""
TELEGRAM_BOT_ID = ""
TELEGRAM_BOT_USERNAME = ""
###############################

def getBotInfo(bot):
    global TELEGRAM_BOT_NAME
    global TELEGRAM_BOT_ID
    global TELEGRAM_BOT_USERNAME

    TELEGRAM_BOT_USERNAME = bot.getMe()['username']
    TELEGRAM_BOT_ID = str(bot.getMe()['id'])
    TELEGRAM_BOT_NAME = bot.getMe()['first_name']

def readtoken(path):
    with open(path, "r") as config:
        token = config.read()

    if token[-1] == "\n":
        token = token[:-1]
    return token

def reply(text, bot_name, bot, chat_id):
    db = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)

    cur = db.cursor()
    cur.execute("SELECT * FROM "+MYSQL_REPLY_TABLE)

    for row in cur.fetchall() :
        if (text == row[0]):
            reply=row[1]
            break
        else:
            reply="Mi dispiace ma non capisco cosa intendi per: \""+text+"\""
    
    return reply

def dbConnection():


def main():
    dbConnection()

    if len(sys.argv) == 1:
        path = "config"
    else:
        path = sys.argv[1]

    #Ottengo il token per la creazione dell'istanza del bot
    TELEGRAM_BOT_TOKEN = readtoken(path)

    #Creazione dell'istanza del bot
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    #Ottengo informazioni del bot
    getBotInfo(bot)

    print ("Avvio bot in corso...")
    print ("Verifica autenticazione..")

    #Stampa identita' del bot
    print ("")
    print ("= Identita' bot =")
    print ("ID: " +TELEGRAM_BOT_ID)
    print ("Nome: " +TELEGRAM_BOT_NAME)
    print ("Username: " +TELEGRAM_BOT_USERNAME)
    print ("")

    #Stampa messaggi ricevuti mentre il bot non era in esecuzione
    print ("Messaggi ricevuti: ")
    updates = bot.getUpdates()
    print ([u.message.text for u in updates])
    print ("")

    print ("Bot avviato!")
    print ("")

    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    #Inizio routine del bot
    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id

            if (text):
                print ("[MSG] "+text)

                #Aggiono informazioni bot
                getBotInfo(bot)

                bot.sendMessage(chat_id=chat_id, text=reply(text, TELEGRAM_BOT_NAME, bot, chat_id))
                LAST_UPDATE_ID = update_id + 1

if __name__ == '__main__':
    main()
