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

import telegram
import sys

TELEGRAM_BOT_NAME="Test Bot"

def readtoken(path):
    with open(path, "r") as config:
        token = config.read()

    if token[-1] == "\n":
        token = token[:-1]
    return token

def reply(text, bot_name, bot):
    if (text == "Come ti chiami?"):
        reply="Di certo non Siri.... Ti pare?!?!?"
    elif (text == "Ti andrebbe un po' di schweppes solo io e te?"):
        reply="No.... Ehi che ti aspettavi?"
        bot.sendPhoto(chat_id=chat_id, photo='http://652af66dabe8673856dc500efee6dfde.s3.amazonaws.com/wp-content/uploads/2011/06/Uma_Thurman_Schweppes_2011-5.jpeg')
    elif (text == "/start"):
        reply="Ciao. Io sono "+bot_name+". Piacere di conoscerti!"
    else:
        reply="Mi dispiace ma non capisco cosa intendi per: \""+text+"\""
    return reply

def main():
    if len(sys.argv) == 1:
        path = "config"
    else:
        path = sys.argv[1]

    TELEGRAM_BOT_TOKEN = readtoken(path)

    print ("Avvio bot in corso...")
    print ("Verifica autenticazione..")

    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    #Stampa identita del bot
    print ("")
    print ("Identita' bot: ")
    print (bot.getMe())
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

                bot.sendMessage(chat_id=chat_id, text=reply(text, TELEGRAM_BOT_NAME, bot))
                LAST_UPDATE_ID = update_id + 1

if __name__ == '__main__':
    main()
