#!/usr/bin/env python
#
# Telepot Bot API v12.6
#
# Copyright (C) 2015
#
# Authors:
# Andrea Crescentini <cresh.it@gmail.com>
# Andrea Bartolucci <andbartol>

import sqlite3
import os
import sys
import telepot
from settings import TOKEN
from time import sleep


TELEGRAM_BOT_USERNAME = ""
TELEGRAM_BOT_ID = ""
TELEGRAM_BOT_NAME = ""

## DATABASE CONNECTION INFO ##
MYSQL_HOST = "localhost"
MYSQL_USER = "telegram"
MYSQL_PASS = "telegram"
MYSQL_DB = "telegram_bot.db"
MYSQL_REPLY_TABLE = "reply"
##############################

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    state = False

    if content_type == 'text' and msg['text'] == '/start':
        bot.sendMessage(chat_id, "Ciao. Io sono " + TELEGRAM_BOT_NAME + ". Piacere di conoscerti!")
    
    if content_type == 'text':
        # Connessione al database
        db = sqlite3.connect(MYSQL_DB)

        # Creazione di un puntatore per scorrere il database
        cur = db.cursor()
        cur.execute("SELECT * FROM " + MYSQL_REPLY_TABLE)
        #cur.execute("SELECT * FROM "+MYSQL_REPLY_TABLE+" WHERE 'message' = '"+text+"'")

        # Esplorazione del database alla ricerca della risposta
        for row in cur.fetchall():
            print (row[1] + " " +row[3])
            if str(msg['text']).lower() == row[1] and row[3] == "text":
                bot.sendMessage(chat_id, row[2])
                state = True
                break

            if str(msg['text']).lower() == row[1] and row[3] == "photo":
                bot.sendMessage(chat_id, row[2])
                state = True
                break

            if str(msg['text']).lower() == row[1] and row[3] == "voice":
                # animazione di dell'immagine file
                bot.sendChatAction(chat_id, 'upload_document')
                # invio dell'immagine dalla cartella
                bot.sendVoice(chat_id, (row[2], open(row[2], 'rb')))
                state = True
                break
                                  
        if state != True:
            # Messaggio di risposta di default
            bot.sendMessage(chat_id, "Mi dispiace ma non capisco cosa intendi per: \"" + msg['text'] + "\"")

# Main
print("Avvio bot in corso...")

# PID file
pid = str(os.getpid())
pidfile = "/tmp/sendreceiver_bot.pid"

# Check if PID exist
if os.path.isfile(pidfile):
    print("%s already exists, exiting!" % pidfile)
    sys.exit()

# Create PID file
f = open(pidfile, 'w')
f.write(pid)

# Start working
try:

    # Creazione dell'istanza del bot
    bot = telepot.Bot(token=TOKEN)
    bot.message_loop(on_chat_message)    
    
    #### Ottengo informazioni del bot ####
    TELEGRAM_BOT_USERNAME = bot.getMe()['username']
    TELEGRAM_BOT_ID = str(bot.getMe()['id'])
    TELEGRAM_BOT_NAME = bot.getMe()['first_name']
    ###########################

    # Stampa identita' del bot
    print ("")
    print ("= Identita' bot =")
    print ("ID: " + TELEGRAM_BOT_ID)
    print ("Nome: " + TELEGRAM_BOT_NAME)
    print ("Username: " + TELEGRAM_BOT_USERNAME)
    print ("")
    print ("Bot avviato!")
    print ("")

    while(1):
        sleep(10)

finally:
    os.unlink(pidfile)